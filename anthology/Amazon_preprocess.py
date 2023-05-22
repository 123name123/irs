import pandas as pd
import numpy as np
import re
import html
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('wordnet')
nltk.download('stopwords')

def check_for_remove_short(x):
    line = ''
    for i in x.split():
        if len(i) > 1:
            line += i + ' '

    return line.strip()
    
def check_for_remove_stopwords(x):
    stop_words = set(stopwords.words('english'))
    line = ''

    for i in x.split():
        if i not in stop_words:
            line += i + ' '

    return line.strip()

def check_len(x, max_len):
    if len(x.split()) <= max_len:
        return x
    else:
        return ' '.join(x.split()[:max_len])

class DataSetPreprocessor:

    def __init__(self) -> None:
        self.data = None

    def fit(self, data: pd.DataFrame) -> None:
        self.data = data

    def transform(self) -> pd.DataFrame:
        self.data.drop(
            columns=['tech1', 'fit', 'also_buy', 'tech2', 'rank', 'also_view', 'details', 'main_cat', 'similar_item',
                     'date', 'asin', 'feature'], inplace=True)
        self.__drop_missing_values()
        self.__remove_lists()
        self.__remove_html()
        self.__additional_transform()
        self.__normalize_whitespace()
        self.data['price'] = self.__get_prices(self.data['price'])
        return self.data

    def fit_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        self.fit(data)
        return self.transform()

    def __drop_missing_values(self):
        self.data = self.data[~self.data['category'].isin([])]
        self.data = self.data[~self.data['description'].isin([])]
        self.data = self.data[self.data.title != '']
        self.data = self.data[self.data.brand != '']
        self.data = self.data[self.data.price != '']
        self.data.reset_index(inplace=True)
        self.data.drop(columns=['index'], inplace=True)

    def __remove_lists(self):
        self.data['category'] = self.data['category'].apply(' '.join)
        self.data['description'] = self.data['description'].apply(' '.join)

    def __remove_html(self):
        self.data['category'] = self.data['category'].apply(lambda x: re.sub('<[^<]+?>', ' ', x))
        self.data['description'] = self.data['description'].apply(lambda x: re.sub('<[^<]+?>', ' ', x))
        self.data['title'] = self.data['title'].apply(lambda x: re.sub('<[^<]+?>', ' ', x))
        self.data['brand'] = self.data['brand'].apply(lambda x: re.sub('<[^<]+?>', ' ', x))

    def __additional_transform(self):
        self.data['category'] = self.data['category'].apply(lambda x: html.unescape(x))
        self.data['description'] = self.data['description'].apply(lambda x: html.unescape(x))
        self.data['title'] = self.data['title'].apply(lambda x: html.unescape(x))
        self.data['brand'] = self.data['brand'].apply(lambda x: html.unescape(x))

    def __normalize_whitespace(self):
        self.data['category'] = self.data['category'].str.replace('  ', ' ')
        self.data['description'] = self.data['description'].str.replace('  ', ' ')
        self.data['title'] = self.data['title'].str.replace('  ', ' ')
        self.data['brand'] = self.data['brand'].str.replace('  ', ' ')

    def __get_prices(self, price):
        all_prices = price.str.extractall(r'(\d\d\.\d\d|\d\.\d\d)')
        all_prices.reset_index(inplace=True)

        temp = []
        for i in range(len(price)):
            temp.append(np.round(np.mean(all_prices[0][all_prices['level_0'] == i].astype('float')), 2))

        return temp
        


class TextPreprocessor:

    def __init__(self):
        self.data = None

    def fit(self, data: pd.DataFrame) -> None:
        self.data = data

    def fit_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        self.fit(data)
        return self.transform()

    def transform(self) -> pd.DataFrame:
        self.__remove_punc()
        self.__normalize_whitespace()
        self.__remove_short()
        self.__lemmatize()
        self.__remove_stopwords()
        self.__shorten()
        self.__remove_numbers()
        return self.data

    def __remove_punc(self):
        pattern = re.compile(r'[^\w\s]+')

        self.data['category'] = self.data['category'].apply(lambda x: re.sub(pattern, ' ', x))
        self.data['description'] = self.data['description'].apply(lambda x: re.sub(pattern, ' ', x))
        self.data['title'] = self.data['title'].apply(lambda x: re.sub(pattern, ' ', x))
        self.data['brand'] = self.data['brand'].apply(lambda x: re.sub(pattern, ' ', x))

    def __normalize_whitespace(self):
        self.data['category'] = self.data['category'].str.replace('  ', ' ')
        self.data['description'] = self.data['description'].str.replace('  ', ' ')
        self.data['title'] = self.data['title'].str.replace('  ', ' ')
        self.data['brand'] = self.data['brand'].str.replace('  ', ' ')

    def __remove_short(self):
        self.data['category'] = self.data['category'].apply(check_for_remove_short)
        self.data['description'] = self.data['description'].apply(check_for_remove_short)
        self.data['title'] = self.data['title'].apply(check_for_remove_short)
        self.data['brand'] = self.data['brand'].apply(check_for_remove_short)

    def __lemmatize(self):
        morph = WordNetLemmatizer()

        self.data['category'] = self.data['category'].apply(lambda x: ' '.join([morph.lemmatize(i.lower()) for i in x.split()]))
        self.data['description'] = self.data['description'].apply(lambda x: ' '.join([morph.lemmatize(i.lower()) for i in x.split()]))
        self.data['title'] = self.data['title'].apply(lambda x: ' '.join([morph.lemmatize(i.lower()) for i in x.split()]))

    def __check_for_remove_stopwords(x):
        stop_words = set(stopwords.words('english'))
        line = ''

        for i in x.split():
            if i not in stop_words:
                line += i + ' '

        return line.strip()

    def __remove_stopwords(self):
        self.data['category'] = self.data['category'].apply(check_for_remove_stopwords)
        self.data['description'] = self.data['description'].apply(check_for_remove_stopwords)
        self.data['title'] = self.data['title'].apply(check_for_remove_stopwords)

    def __shorten(self):
        self.data['category'] = self.data['category'].apply(lambda x: check_len(x, 53))
        self.data['description'] = self.data['description'].apply(lambda x: check_len(x, 134))
        self.data['title'] = self.data['title'].apply(lambda x: check_len(x, 13))
    
    def __remove_numbers(self):
        self.data['category'] = self.data['category'].apply(lambda x: re.sub('(\d)', '', x))
        self.data['description'] = self.data['description'].apply(lambda x: re.sub('(\d)', '', x))
        self.data['title'] = self.data['title'].apply(lambda x: re.sub('(\d)', '', x))
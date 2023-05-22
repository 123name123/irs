import django_filters

from shop.models import Product, Category


class ProductsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr='istartswith')
    category = django_filters.CharFilter(field_name="app_category__name", lookup_expr='istartswith')
    category_id = django_filters.CharFilter(field_name="app_category__id", lookup_expr='iexact')
    supplier_name = django_filters.CharFilter(field_name="supplier__name", lookup_expr='iexact')
    brand = django_filters.CharFilter(field_name="brand", lookup_expr='iexact')
    price = django_filters.NumberFilter(field_name='price')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        model = Product
        fields = ['title',
                  'category',
                  'category_id',
                  'is_available',
                  'color',
                  'price__gt',
                  'price__lt',
                  'supplier_name',
                  'brand']


class CategoriesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Category
        fields = ['name']

### Запуск:
#### включить docker 
    docker compose up


POST http://127.0.0.1:8000/api/auth/users/ зарегистрироваться {"username": "", "password":""}
POST http://127.0.0.1:8000/api/auth/token/login/  получить токен {"username": "", "password":""}
GET http://127.0.0.1:8000/api/auth/users/ посмотреть пользователей
GET http://127.0.0.1:8000/api/auth/users/me/ посмотреть информацию о себе (под токеном)
POST http://127.0.0.1:8000/api/auth/token/logout/ удалить токен

GET http://127.0.0.1:8000/api/v1/products/ все товары
GET http://127.0.0.1:8000/api/v1/products/1/ конкретный товар
GET http://127.0.0.1:8000/api/v1/categories/ все категории
GET http://127.0.0.1:8000/api/v1/categories/1/ конкретную категорию
GET http://127.0.0.1:8000/api/v1/suppliers/ все поставщики
GET http://127.0.0.1:8000/api/v1/suppliers/1/ конкретный поставщик

GET http://127.0.0.1:8000/api/v1/favorites/ посмотреть все свои подписки
GET http://127.0.0.1:8000/api/v1/favorites/1/ проверить свою подписку на товар с ID 1
POST http://127.0.0.1:8000/api/v1/favorites/ подписаться на товар 1 {"product_id":"1"}
DELETE http://127.0.0.1:8000/api/v1/favorites/1/ удалить свою подписку на товар с ID 1

  #app_category это и есть категория, а category в product это supplier_category таблица

База с продуктами работает долго, если например искать по заголовку в продуктах, 
так как там большое количество записей в таблице с продуктами и база отвечает очень долго.

      GET  http://127.0.0.1:8000/api/v1/products/?is_available=1 # посмотреть все товары которые доступны
      GET  http://127.0.0.1:8000/api/v1/products/?category=Aire #посмотреть товары с категорией у которых есть слово
      GET  http://127.0.0.1:8000/api/v1/products/?category_id=1.04.01.01 #посмотреть товары с id категорией с **точным совпадением слова**
      GET  http://127.0.0.1:8000/api/v1/products/?supplier_name=walmarkt #посмотреть товары с supplier_name с **точным совпадением слова**
      GET  http://127.0.0.1:8000/api/v1/products/?title=walmarkt #посмотреть товары с title у которых есть слово
      GET  http://127.0.0.1:8000/api/v1/products/?color=black #посмотреть товары с color с **точным совпадением слова**
      GET  http://127.0.0.1:8000/api/v1/products/?brand=walmarkt #посмотреть товары с brand с **точным совпадением слова**
      GET  http://127.0.0.1:8000/api/v1/products/?price__gt=100&price__lt=1000 #посмотреть товары больше 100 и меньше 1000
      GET  http://127.0.0.1:8000/api/v1/products/?ordering=brand,-color # можно также сортировать по любому или нескольким полям (через запятую, знак минуса для обратной сортировки)
      GET GET http://127.0.0.1:8000/api/v1/products/?ordering=id все категории сортировка по id

      GET  http://127.0.0.1:8000/api/v1/categories/?name=Aire #посмотреть категории у которых в name есть слово

      (ввод слов case insensetive, то есть что большими что маленькими)

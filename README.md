# barkol
Корпоративный сайт Авиакомпания "БАРКОЛ"
>Установить все необходимые зависимости для уже готового проекта:
```
pip install -r requirements.txt
```

>Создание миграций:
```
manage.py makemigrations
manage.py migrate
```

>Загрузка базы:
```
manage.py loaddata edo\fixtures\address.json
manage.py loaddata edo\fixtures\person.json

manage.py loaddata edo\fixtures\access.json
manage.py loaddata edo\fixtures\category.json
manage.py loaddata edo\fixtures\document.json
```

>Данные пользователя:
```
admin:admin
```

### Инструкции для экспорта готовой БД
>Выгрузка базы:
```
manage.py dumpdata authapp.Person > edo\fixtures\person.json
manage.py dumpdata authapp.Address > edo\fixtures\address.json

manage.py dumpdata libapp.AccessLevel > edo\fixtures\access.json
manage.py dumpdata libapp.Category > edo\fixtures\category.json
manage.py dumpdata libapp.Document > edo\fixtures\document.json
```
[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
# REST АПИ для воображаемого клиентского приложения, которое должно отображать страницу со списком студентов

## Описание
У студента есть поля:
- ФИО
- дата рождения
- успеваемость (опционально из справочника неуд/уд/хор/отл)

## Возможности:
1) добавить нового студента в этот список;
2) удалить существующего студента;
3) отредактировать существующего студента;
4) аутентификация по JWT

## Установка:
1. Клонируйте репозиторий на локальную машину.
- ``git clone https://github.com/da-semenov/Loft_test``
2. Установите виртуальное окружение в корневой директории api_students
- ``python -m venv venv``
3. Активируйте виртуальное окружение.
- ``source venv/bin/activate``
4. Установите зависимости.
- ``pip install -r requirements.txt``
5. Выполните миграции.
- ``python manage.py migrate``
6. Создайте суперпользователя.
- ``python manage.py createsuperuser``
7. Запустите локальный сервер.
- ``python manage.py runserver``
8. Получите JWT-токен. Выполните POST-запрос передав поля username и password
- ``localhost:8000/api/v1/token/``
   Токен вернётся в поле access
9. При отправке запросов передавайте токен в заголовке Authorization: Bearer <токен>

## Доступные эндпоинты:
```
GET                       /               - возвращает список эндпоинтов
GET, POST                 /students/      - просмотр списка студентов, добавление новых
GET, PUT, PATCH, DELETE   /students/{id}/ - просмотр, измение, удаление записи о студенте
```
## Документация:
```
GET                       /swagger-ui        - Swagger
GET                       /redoc             - Redoc
```

## Основные использованные технологии
* [python 3.8](https://www.python.org/)
* [django](https://www.djangoproject.com/)
* [drf](https://www.django-rest-framework.org/)
* [swagger](https://swagger.io/)
* [redoc](https://redoc.ly/redoc/)

## Автор
* **Семенов Денис** - [da-semenov](https://github.com/da-semenov)
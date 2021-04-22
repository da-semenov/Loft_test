[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
# Небольшой движок блога на Django Framework
Блог с возможностью публикации постов с тегами и комментариями.

# Описание
ПУБЛИКАЦИЯ
- заголовок
- дата создания (авто)
- текст
- список тэгов

Новая публикация добавляется не через Django Admin, а через самописную админку.
Отображается по 10 публикаций на страницу.
Тэги создаются и прикрепляются к публикации через админку.
Около публикации показывается кол-во комментариев. 
На странице публикации любой может оставить комментарий.


## Установка:
1. Клонируйте репозиторий на локальную машину.
- ``git clone https://github.com/da-semenov/Loft_test``
2. Установите виртуальное окружение в корневой директории blog.
- ``python -m venv venv``
3. Активируйте виртуальное окружение.
- ``source venv/Scripts/activate``
4. Установите зависимости.
- ``pip install -r requirements.txt``
5. Запустите локальный сервер.
- ``python manage.py runserver``

Создание новой публикации: http://127.0.0.1:8000/new/

Тестовая база и суперпользователь уже созданы
Админка Django:
user: admin
password: admin

## Основные использованные технологии
* [python 3.8](https://www.python.org/)
* [django 3.2](https://www.djangoproject.com/)

## Автор

* **Семенов Денис** - [da-semenov](https://github.com/da-semenov)

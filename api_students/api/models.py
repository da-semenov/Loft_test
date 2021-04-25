from django.db import models


class Student(models.Model):

    class Grade(models.IntegerChoices):
        EXCELLENT = 5, 'Отлично'
        GOOD = 4, 'Хорошо'
        SATISFACTORY = 3, 'Удовлетворительно'
        UNSATISFACTORY = 2, 'Неудовлетворительно'

    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    patronymic = models.CharField(max_length=255, blank=True,
                                  verbose_name='Отчество')
    birthday = models.DateField(blank=True, null=True, db_index=True,
                                verbose_name='Дата рождения')
    grade = models.SmallIntegerField(choices=Grade.choices, blank=True,
                                     null=True, verbose_name='Успеваемость')

from django.contrib import admin

from api.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'surname', 'name', 'patronymic',
                    'birthday', 'grade')
    search_fields = ('surname',)
    list_filter = ('grade',)
    empty_value_display = '-пусто-'


admin.site.register(Student, StudentAdmin)

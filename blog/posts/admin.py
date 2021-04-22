from django.contrib import admin

from .models import Comment, Post, Tag


class PostAdmin(admin.ModelAdmin):
    """
    Конфигурация модели в admin.py.
    """

    list_display = ('pk', "title", 'pub_date', 'text', 'tags')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post', 'text', 'created')
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    search_fields = ('title',)


"""
Регистрация моделей в админке django.
"""

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

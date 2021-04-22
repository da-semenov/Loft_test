from django.forms import ModelForm

from .models import Comment, Post


class PostForm(ModelForm):
    """
    Класс для формы создания новой публикации.
    """

    class Meta:
        # на основе какой модели создаётся класс формы
        model = Post
        # указываем, какие поля будут в форме
        fields = ['title', 'tags', 'text']
        # метка поля
        labels = {'title': "Заголовок", 'tags': 'Тэг', 'text': 'Текст'}
        # вспомогательный текст, который привязан к полю
        help_texts = {'title': 'Введите заголовок',
                      'tags': 'Выберите тэг',
                      'text': 'Введите текст публикации'}


class CommentForm(ModelForm):
    """
    Класс для формы комментариев.
    """

    class Meta:
        model = Comment
        fields = ('text', )
        labels = {'text': 'Комментарий'}

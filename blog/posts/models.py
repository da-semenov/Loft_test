from django.db import models


class Tag(models.Model):
    """
    Модель Тэгов.
    """

    title = models.CharField(max_length=64, verbose_name='Название тэга')

    def __str__(self):
        return self.title


class Post(models.Model):
    """
    Модель для публикации.
    """

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата создания')
    text = models.TextField(verbose_name='Текст')
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True,
                             related_name='posts', verbose_name='Тэг')

    class Meta:
        """
        Сортируем по времени создания публикации.
        """
        ordering = ['-pub_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Модель комментария.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Публикация')
    text = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return '{} on {}'.format(self.post, self.created)

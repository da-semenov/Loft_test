from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .forms import CommentForm, PostForm
from .models import Post


def index(request):
    """
    Представление предоставляет опубликованные сообщения в index.html.
    request: объект запроса,
    return: context:словарь со списком публикаций с учетом разбивки
    на страницы.
    """

    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page')
    page_posts = paginator.get_page(page)

    context = {
        'posts': page_posts
    }
    return render(request, 'index.html', context)


def new_post(request):
    """
    Представление для создания новой публикации.
    request: объект запроса,
    return: form: словарь с данными конкретной публ.
    """

    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('posts:index')
    return render(request, 'new.html', {'form': form})


def post_page(request, post_id):
    """
    Представление предоставляет полный текст и комментарии к конкретной
    публикации.
    request: объект запроса
    post_id: id для конкретной публ., которая будет отображаться на странице
    return: context:словарь с данными конкретной публ. и её комментариями
    """

    post = Post.objects.get(id=post_id)
    comments = post.comments
    new_comment = None
    form = CommentForm(request.POST or None)
    if form.is_valid():
        # сохраняем новый комментарий и связываем его с публ.
        new_comment = form.save(commit=False)
        new_comment.post = post
        new_comment.save()
        return redirect('posts:post', post_id)
    comment_form = CommentForm()
    context = {'post': post,
               'comments': comments,
               'new_comment': new_comment,
               'comment_form': comment_form
               }
    return render(request, 'post.html', context)

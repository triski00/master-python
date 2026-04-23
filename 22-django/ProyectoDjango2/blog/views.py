from django.shortcuts import render
from blog.models import Article

def list(request):
    articles = Article.objects.all()

    return render(request, 'articles/list.html', {
        'title': 'Artículos',
        'articles': articles
    })

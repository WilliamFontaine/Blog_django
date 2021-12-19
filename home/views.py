from django.shortcuts import render
from .models import Article


# Create your views here.

def index(request):
    articles = Article.objects.all()
    data = {'articles':articles}
    return render(request, 'home/index.html', data)


def article(request, name):
    try:
        article = Article.objects.get(titre=name)
        data = {'article':article}   
    except:
        data = {'erreur':'l\'article que vous avez demandé n\'existe pas !'}
    return render(request, 'home/article.html', data)
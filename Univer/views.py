from django.shortcuts import render
from .models import Categories, News


def index(request):
    category = Categories.objects.all()
    news = News.objects.all()

    return render(request, 'news/index.html', {'category': category, 'news': news})

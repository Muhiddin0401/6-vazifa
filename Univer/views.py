from django.shortcuts import render
from .models import Categories, News


def index(request):
    category = Categories.objects.all()
    news = News.objects.all()

    return render(request, 'news/index.html', {'category': category, 'news': news})

def category_new(request,category_id):
    category = Categories.objects.all()
    news = News.objects.filter(id=category_id)
    context = {
        "category": category,
        "news": news
    }

    return render(request, 'news/index.html', context)

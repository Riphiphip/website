from django.shortcuts import render
from news.models import Article,Event, Thumbnail


def index(request):
    event_list = Event.objects.order_by('-event_date')
    article_list = Article.objects.order_by('-pub_date')[:3]
    thumbnail_list = Thumbnail.objects.all()
    context = {
        'article_list': article_list,
        'thumbnail_list': thumbnail_list,
        'event_list': event_list,
    }

    return render(request, 'index.html', context)
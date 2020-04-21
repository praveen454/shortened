from django.shortcuts import render
from django.http import HttpResponse
from .models import ShortendUrl

# Create your views here.

def home(request):

    url1 = ShortendUrl()
    url1.id = 1
    url1.longurl = 'https://www.youtube.com'
    url1.shorturl = 'https://www.youtube.com'

    url2 = ShortendUrl()
    url2.id = 2
    url2.longurl = 'https://www.youtube.com'
    url2.shorturl = 'https://www.youtube.com'


    return render(request, 'shortenedurl.html', {'shortenedUrlList': [url1, url2]})
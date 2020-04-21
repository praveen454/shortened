from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name='shortenedurl'),
    path('create_shortner',views.urlshortner,name='create_shortner')
]



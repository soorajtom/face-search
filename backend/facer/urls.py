
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from .views import index, results, search, protected_serve

urlpatterns = [
    path('', index),
    path('search/', search, name="search"),
    re_path(r'^results\/(?P<token>[\w\d-]{0,50})\/?$', results, name="results"),
    re_path(r'^{}(?P<path>.*)$'.format(settings.MEDIA_URL[1:]), protected_serve),
]

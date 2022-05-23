from unicodedata import name
from django.urls import re_path as url
from . import views

urlpatterns =[
    url('^$',views.welcome,name = 'Welcome'),
    url('^today/$',views.news_of_day,name= 'newsToday'),
  
]

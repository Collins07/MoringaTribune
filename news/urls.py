from unicodedata import name
from django.conf.urls import url
from . import views

urlpatterns =[
    url('^$',views.welcome,name = 'Welcome'),
]
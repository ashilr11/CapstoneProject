#this is where we set up the mappings from certain urls to where we send the user. Maps urls to certain html web pages

from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='App-home'),
    path('adddata/', views.adddata, name='App-adddata'),
    path('datacards/', views.datacards, name='App-datacards'),
    path('help/', views.help, name='App-help'),
    path('about/', views.about, name='App-about'),
]

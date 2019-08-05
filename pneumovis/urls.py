from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='App-home'),
    path('adddata/', views.adddata, name='App-adddata'),
    path('datacards/', views.datacards, name='App-datacards'),
    path('help/', views.help, name='App-help'),
    path('about/', views.about, name='App-about'),
]

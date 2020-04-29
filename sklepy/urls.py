from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('formularz/', views.formularz, name='formularz'),
    path('widok/', views.widok, name='widok')
]
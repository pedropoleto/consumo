from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('visualizar/', views.visualizar, name='visualizar'),
    path('saida/<int:pk>/', views.saida, name='saida')
]

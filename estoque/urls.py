from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('visualizar/', views.visualizar, name='visualizar'),
    path('saida_material/<int:pk>/', views.saida_material, name='saida_material')
]

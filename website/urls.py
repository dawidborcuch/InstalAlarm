from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('realizacje/', views.realizacje, name='realizacje'),
    path('polityka-prywatnosci/', views.polityka_prywatnosci, name='polityka_prywatnosci'),
]

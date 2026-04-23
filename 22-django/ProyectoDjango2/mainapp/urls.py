from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('hola-mundo/', views.hola_mundo, name='hola_mundo'),

]
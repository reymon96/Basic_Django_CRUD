from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.register),
    path('edicion/<codigo>', views.edit),
    path('edicion/update/', views.update),
    path('eliminacion/<codigo>', views.delete)
]

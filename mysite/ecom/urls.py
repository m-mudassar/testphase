import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name="add"),
    path('update', views.add, name="update"),
    path('delete', views.delete, name="delete"),
    path('search', views.search, name="search"),
    path('add_service', views.add_service, name="add_service"),
    path('update_service', views.update_service, name="update_service"),
    path('delte_service', views.delete_service, name="delete_service")
]

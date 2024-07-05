from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

from . import views

app_name="todo"
urlpatterns = [
    path('', views.index_view, name='index'),
    path('add/', views.create_problem, name='add'),
    path('delete/', views.delete_problem, name='delete')
]

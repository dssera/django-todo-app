from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('', views.index_view),
    path('add/', views.create_problem),
    path('delete/', views.delete_problem)
]

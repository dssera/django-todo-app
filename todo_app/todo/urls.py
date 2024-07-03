from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('', views.say_hello_view)
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'), # this is the home page of cars app
]

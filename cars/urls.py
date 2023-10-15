from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars, name='cars'), # this is the home page of cars app
    path('<int:id>', views.car_details, name='car_details'), # this is the car detail page
    path('search', views.search, name='search'), # this is the search page
]

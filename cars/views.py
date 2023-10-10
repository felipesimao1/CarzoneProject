from django.shortcuts import render

# Create your views here.

def cars(request):
    return render(request, 'cars/cars.html') # this is the home page of cars app inside templates/cars/cars.html
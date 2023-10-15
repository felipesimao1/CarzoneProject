from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import Paginator

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date') # this is the car model inside models.py
    paginator = Paginator(cars, 4) # Show 4 cars per page.
    page = request.GET.get('page') # this is the page number
    page_cars = paginator.get_page(page) # this is the page number
    data = {
        'cars': page_cars # this is the cars variable

    }
    return render(request, 'cars/cars.html', data) # this is the home page of cars app inside templates/cars/cars.html

def car_details(request, id):
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car': single_car
    }
    return render(request, 'cars/car_details.html', data) # this is the car detail page inside templates/cars/car_details.html

def search(request):

    cars = Car.objects.order_by('-created_date')
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_type' in request.GET:
        body_type = request.GET['body_type']
        if body_type:
            cars = cars.filter(body_type__iexact=body_type)

    data = {
        'cars': cars,
    }

    return render(request, 'cars/search.html', data) # this is the search page inside templates/cars/search.html
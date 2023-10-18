from django.shortcuts import get_object_or_404, render 
from django.core.paginator import Paginator
from .models import Car

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date') # this is the car model inside models.py
    paginator = Paginator(cars, 4) # Show 4 cars per page.
    page = request.GET.get('page') # this is the page number
    page_cars = paginator.get_page(page) # this is the page number

    car_title_search = Car.objects.values('car_title').distinct() # get all the objects from the Car model and values of the car_title field
    city_search = Car.objects.values('city').distinct() # get all the objects from the Car model and values of the city field
    year_search = Car.objects.values('year').distinct() # get all the objects from the Car model and values of the year field
    body_type_search = Car.objects.values('body_type').distinct() # get all the objects from the Car model and values of the body_type field


    data = {
        'cars': page_cars, # this is the cars variable
        'car_title_search': car_title_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_type_search': body_type_search,
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

    car_title_search = Car.objects.values('car_title').distinct() # get all the objects from the Car model and values of the car_title field
    city_search = Car.objects.values('city').distinct() # get all the objects from the Car model and values of the city field
    year_search = Car.objects.values('year').distinct() # get all the objects from the Car model and values of the year field
    body_type_search = Car.objects.values('body_type').distinct() # get all the objects from the Car model and values of the body_type field
    
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


    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'car_title_search': car_title_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_type_search': body_type_search,
    }

    return render(request, 'cars/search.html', data) # this is the search page inside templates/cars/search.html
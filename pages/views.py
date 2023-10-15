from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.

def home(request):
    teams = Team.objects.all() # get all the objects from the Team model
    is_published = Car.objects.order_by('-created_date').filter(is_published=True) # get all the objects from the Car model ordered by the created_date and filtered by is_featured
    #search_fields = Car.objects.values('city', 'year', 'body_type', 'engine', 'transmission') # get all the objects from the Car model and values of the fields
    
    car_title_search = Car.objects.values('car_title').distinct() # get all the objects from the Car model and values of the car_title field
    city_search = Car.objects.values('city').distinct() # get all the objects from the Car model and values of the city field
    year_search = Car.objects.values('year').distinct() # get all the objects from the Car model and values of the year field
    body_type_search = Car.objects.values('body_type').distinct() # get all the objects from the Car model and values of the body_type field

    data = {
        'teams': teams,
        'is_published': is_published,
        #'search_fields': search_fields,
        'body_type_search': body_type_search,
        'car_title_search': car_title_search,
        'city_search': city_search,
        'year_search': year_search,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all() # get all the objects from the Team model
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html',data)
 
def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
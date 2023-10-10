from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.

def home(request):
    teams = Team.objects.all() # get all the objects from the Team model
    is_published = Car.objects.order_by('-created_date').filter(is_published=True) # get all the objects from the Car model ordered by the created_date and filtered by is_featured
    data = {
        'teams': teams,
        'is_published': is_published,
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
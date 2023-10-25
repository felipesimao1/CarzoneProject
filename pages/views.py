from django.shortcuts import render
from .models import Team
from cars.models import Car
from contacts.models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        email_subject = 'You have a new message from ' + name + ' about ' + subject + '!'
        message_body = 'Name: ' + name + '\nEmail: ' + email + '\nPhone: ' + phone + '\nMessage: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            'felipe.simao1@outlook.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Your message has been sent successfully')
        return render(request, 'pages/contact.html', {'success': True})
    
    return render(request, 'pages/contact.html')
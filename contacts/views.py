from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.

def inquiry(request):

    # recebe os dados do formulário de contato
    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        car_title = request.POST.get('car_title')
        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        city = request.POST.get('city')
        country = request.POST.get('country')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Verifica se o usuário já fez uma pergunta sobre o mesmo carro
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this car')
                return redirect('/cars/'+car_id)

        contact = Contact(car_id=car_id,
                          car_title=car_title, 
                          first_name=first_name,
                          last_name=last_name, 
                          city=city,
                          country=country, 
                          email=email, 
                          phone=phone,
                          message=message, 
                          user_id=user_id,
                          )
        
        # Envia um email para o administrador
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        email_subject = 'You have a new message from ' + first_name + ' ' + last_name
        message_body = 'Name: ' + first_name + ' ' + last_name + '\nEmail: ' + email + '\nPhone: ' + phone + '\nMessage: ' + message
        send_mail(
            email_subject,
            message_body,
            'felipe.simao1@outlook.com',
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        
        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')   
        return redirect('/cars/'+car_id)
   
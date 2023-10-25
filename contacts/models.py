from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car_id = models.IntegerField()
    custumer_need = models.CharField(max_length=200)
    car_title = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    user_id = models.IntegerField()   
    created_date = models.DateTimeField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.email
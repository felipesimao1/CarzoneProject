from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=200)
    twitter_link = models.URLField(max_length=200)
    google_plus_link = models.URLField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return '{}'.format(self.first_name)
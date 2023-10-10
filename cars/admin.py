from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import Car

class CarAdmin(admin.ModelAdmin):   
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo_main.url))
     
    list_display = ('id' , 'thumbnail', 'car_title', 'year', 'city', 'country', 'is_published')
    list_display_links = ('id', 'car_title', 'thumbnail')
    list_editable = ('is_published',)
    search_fields = ('car_title', 'city', 'country', 'year')
    list_filter = ('city', 'country')
admin.site.register(Car, CarAdmin) # this is to register the Car model in the admin page


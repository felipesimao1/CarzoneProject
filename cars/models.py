from django.db import models


# Create your models here.

class Car(models.Model):
    country_choices = {
        ('BR', 'Brazil'),
        ('IRE', 'Ireland'),
        ('UK', 'United Kingdom'),
        ('US', 'United States'),        
    }
    city_choices = {
        ('Dublin', 'Dublin'),
        ('London', 'London'),
        ('New York', 'New York'),
        ('Sao Paulo', 'Sao Paulo'),        
    }
    color_choices = {
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Red', 'Red'),
        ('White', 'White'),
        ('Yellow', 'Yellow'),
        ('Grey', 'Grey')        
    }
    body_type_choices = {
        ('Convertible', 'Convertible'),
        ('Coupe', 'Coupe'),
        ('Hatchback', 'Hatchback'),
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Van', 'Van'),        
    }
    engine_choices = {
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Gas', 'Gas'),
        ('Hybrid', 'Hybrid'),
        ('Petrol', 'Petrol'),        
    }
    engine_size_choices = {
        ('1.0', '1.0'),
        ('1.5', '1.5'),
        ('2.0', '2.0'),
        ('3.2', '3.2'),
        ('4.0', '4.0'),
    }
    transmission_choices = {
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),        
    }
    featured_choices = {
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    }


    car_title = models.CharField(max_length=200)
    country = models.CharField(max_length=200, choices = country_choices)
    city = models.CharField(max_length=200, choices = city_choices)
    color = models.CharField(max_length=200, choices = color_choices)
    year = models.IntegerField()
    price = models.IntegerField()
    body_type = models.CharField(max_length=200, choices = body_type_choices)
    description = models.TextField(max_length=2000)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # blank=True means this field is optional
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # blank=True means this field is optional
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # blank=True means this field is optional
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # blank=True means this field is optional
    engine = models.CharField(max_length=200, choices = engine_choices)
    engine_size = models.IntegerField()
    transmission = models.CharField(max_length=200, choices = transmission_choices)
    feature1 = models.CharField(max_length=200, choices = featured_choices, blank=True)
    feature2 = models.CharField(max_length=200, choices = featured_choices, blank=True)
    feature3 = models.CharField(max_length=200, choices = featured_choices, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.car_title


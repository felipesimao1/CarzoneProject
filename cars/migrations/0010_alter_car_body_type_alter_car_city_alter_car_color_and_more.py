# Generated by Django 4.2.5 on 2023-10-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_body_type_alter_car_city_alter_car_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('Coupe', 'Coupe'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('Van', 'Van'), ('Convertible', 'Convertible'), ('SUV', 'SUV')], max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.CharField(choices=[('Sao Paulo', 'Sao Paulo'), ('Dublin', 'Dublin'), ('New York', 'New York'), ('London', 'London')], max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Blue', 'Blue'), ('Yellow', 'Yellow'), ('Red', 'Red'), ('Grey', 'Grey'), ('Green', 'Green')], max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='country',
            field=models.CharField(choices=[('IRE', 'Ireland'), ('UK', 'United Kingdom'), ('BR', 'Brazil'), ('US', 'United States')], max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(choices=[('Electric', 'Electric'), ('Petrol', 'Petrol'), ('Hybrid', 'Hybrid'), ('Gas', 'Gas'), ('Diesel', 'Diesel')], max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='feature1',
            field=models.CharField(blank=True, choices=[('Alarm System', 'Alarm System'), ('Audio Interface', 'Audio Interface'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Wind Deflector', 'Wind Deflector'), ('Power Steering', 'Power Steering'), ('Cruise Control', 'Cruise Control'), ('Seat Heating', 'Seat Heating'), ('ParkAssist', 'ParkAssist'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Bluetooth Handset', 'Bluetooth Handset'), ('Air Conditioning', 'Air Conditioning'), ('Airbags', 'Airbags')], max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='feature2',
            field=models.CharField(blank=True, choices=[('Alarm System', 'Alarm System'), ('Audio Interface', 'Audio Interface'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Wind Deflector', 'Wind Deflector'), ('Power Steering', 'Power Steering'), ('Cruise Control', 'Cruise Control'), ('Seat Heating', 'Seat Heating'), ('ParkAssist', 'ParkAssist'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Bluetooth Handset', 'Bluetooth Handset'), ('Air Conditioning', 'Air Conditioning'), ('Airbags', 'Airbags')], max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='feature3',
            field=models.CharField(blank=True, choices=[('Alarm System', 'Alarm System'), ('Audio Interface', 'Audio Interface'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Wind Deflector', 'Wind Deflector'), ('Power Steering', 'Power Steering'), ('Cruise Control', 'Cruise Control'), ('Seat Heating', 'Seat Heating'), ('ParkAssist', 'ParkAssist'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Bluetooth Handset', 'Bluetooth Handset'), ('Air Conditioning', 'Air Conditioning'), ('Airbags', 'Airbags')], max_length=200),
        ),
    ]
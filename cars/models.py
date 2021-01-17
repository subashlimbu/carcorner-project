from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

    state_choice = (
        ('AV', 'Avon'),
        ('BE', 'Bedfordshire'),
        ('BK', 'Berkshire'),
        ('BU', 'Buckinghamshire'),
        ('CA', 'Cambridgeshire'),
        ('CH', 'Cheshire'),
        ('CV', 'Cleveland'),
        ('CO', 'Cornwall'),
        ('CD', 'Cumberland'),
        ('CU', 'Cumbria'),
        ('DE', 'Derbyshire'),
        ('DV', 'Devon'),
        ('DO', 'Dorset'),
        ('DU', 'County Durham'),
        ('EX', 'Essex'),
        ('GE', 'Gloucestershire'),
        ('GL', 'Greater London'),
        ('GM', 'Greater Manchester'),
        ('HA', 'Hampshire'),
        ('HE', 'Herefordshire'),
        ('HT', 'Hertfordshire'),
        ('HB', 'Humberside'),
        ('HU', 'Huntingdonshire'),
        ('IW', 'Isle of Wight'),
        ('KE', 'Kent'),
        ('LA', 'Lancashire'),
        ('LE', 'Leicestershire'),
        ('LN', 'Lincolnshire'),
        ('LON', 'London'),
        ('ME', 'Merseyside'),
        ('MX', 'Middlesex'),
        ('NO', 'Norfolk'),
        ('NH', 'Northamptonshire'),
        ('ND', 'Northumberland'),
        ('NT', 'Nottinghamshire'),
        ('OX', 'Oxfordshire'),
        ('RU', 'Rutland'),
        ('SH', 'Shropshire'),
        ('SO', 'Somerset'),
        ('ST', 'Staffordshire'),
        ('SK', 'Suffolk'),
        ('SU', 'Surrey'),
        ('SX', 'Sussex'),
        ('TW', 'Tyne and Wear'),
        ('WA', 'Warwickshire'),
        ('WM', 'West Midlands'),
        ('WE', 'Westmorland'),
        ('WI', 'Wiltshire'),
        ('WO', 'Worcestershire'),
        ('YO', 'Yorkshire'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
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
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title

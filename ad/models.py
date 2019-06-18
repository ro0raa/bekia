from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ad(models.Model):
    MAIN_CATEGORY = [
        ('VEH', 'Vehicles'),
        ('PRO', 'Properties'),
        ('MOB&Acc', 'Mobile Phones & Accessories'),
        ('ELE&HOAPP', 'Electronics & Home Appliances'),
        ('HO&GA', 'Home & Garden'),
        ('FAS&BEA', 'Fashion & Beauty'),
        ('PET', 'Pets'),
        ('Kid', 'Kids & Babies'),
        ('SPORT', 'Sporting Goods & Bikes'),
        ('HOB', 'Hobbies, Music, Art & Books'),
        ('JOB', 'Jobs'),
        ('BUSS', 'Business & Industrial'),
        ('SER', 'Services'),

    ]
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    main_category = models.CharField(choices=MAIN_CATEGORY, max_length=50)
    description = models.TextField()
    photos = models.FileField(upload_to='Images/%Y-%m-%d/')
    city = models.CharField(max_length=120)
    Mobile_phone_number = models.CharField(max_length=11)





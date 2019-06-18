from django.db import models
from django.contrib.auth.models import User



class advertisement(models.Model):
	
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.TextField(max_length=70)
	type_choices=[(0,'cars'),(1,'real estates'),(2,'mobiles'),(3,'electronics'),(4,'house'),(5,'fashion'),(6,'animals'),(7,'baby staff'),(8,'music') ,(9,'jobs'),(10,'trade'),(11,'services')]
	adv_type=models.CharField(choices=type_choices,max_length=3)
	desc=models.TextField(max_length=8069)
	name= models.TextField()
	city= models.TextField(max_length=30)
	mob= models.TextField(max_length=12)
	email=models.EmailField()
	connectedby_choices=[(0,'both'),(1,'mob'),(2,'olx email')]
	connectby=models.CharField(choices=connectedby_choices,max_length=2)

class images(models.Model):
	advertisement=models.ForeignKey(advertisement,on_delete=models.CASCADE)
	image=models.FileField(upload_to="media/")









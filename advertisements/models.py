from django.db import models
from django.contrib.auth.models import User

class AdvTypes(models.Model):
	name=models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Advertisement(models.Model):
	
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=70,blank=False)
	#type_choices=[(0,'cars'),(1,'real estates'),(2,'mobiles'),(3,'electronics'),(4,'house'),(5,'fashion'),(6,'animals'),(7,'baby staff'),(8,'music') ,(9,'jobs'),(10,'trade'),(11,'services')]
	adv_type=models.ForeignKey(AdvTypes,on_delete=models.CASCADE)
	desc=models.TextField(max_length=8069,blank=False)
	name= models.CharField(max_length=100,blank=False)
	city= models.CharField(max_length=30,blank=False)
	mob= models.CharField(max_length=12,blank=False)
	email=models.EmailField(blank=False)	
	connectedby_choices=[(1,'both'),(2,'mob'),(3,'olx email')]
	connectby=models.IntegerField(choices=connectedby_choices,default=0)
	def __str__(self):
		return self.title

class Images(models.Model):
	advertisement=models.ForeignKey(Advertisement,on_delete=models.CASCADE)
	image=models.FileField(upload_to="images/")
	order=models.IntegerField(default=0)









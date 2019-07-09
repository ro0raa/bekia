from django.forms import ModelForm
from .models import Advertisement,Images

class AdvForm(ModelForm):
     class Meta:
     	model=Advertisement
     	exclude = ['user']



class ImageForm(ModelForm):
	class Meta:
		model=Images
		exclude=['order']



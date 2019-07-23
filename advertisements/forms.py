from django.forms import ModelForm
from .models import Advertisement,Images
from django import forms
class AdvForm(ModelForm):
	class Meta:
		model=Advertisement
		exclude = ['user']
		widgets = {
            'mob': forms.NumberInput(), }



class ImageForm(ModelForm):
	class Meta:
		model=Images
		exclude=['order']



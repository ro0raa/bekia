from django.forms import ModelForm
from .models import Advertisement

class AdvForm(ModelForm):
     class Meta:
     	model=Advertisement
     	exclude = ['user']



from django.forms import ModelForm
from app.models import Cooperative
from app.models import Membre
from django import forms



class CooperativeForm(ModelForm):
    class Meta:
        model = Cooperative
        fields = '__all__'
      
    
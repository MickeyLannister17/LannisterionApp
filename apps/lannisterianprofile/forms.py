from django import forms
from django.forms import fields

from .models import LannisterianProfile

class LannisterianProfileForm(forms.ModelForm):
    
    class Meta:
        model = LannisterianProfile
        fields = ('avatar',)
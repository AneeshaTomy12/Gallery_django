from pyexpat import model
from django import forms
from .models import Imgmodel

class ImageForm(forms.ModelForm):
    class Meta:
        model=Imgmodel
        fields='__all__'
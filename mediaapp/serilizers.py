from pyexpat import model
from rest_framework import serializers
from .models import Imgmodel

class GallerySerilizer(serializers.ModelSerializer):
    class Meta:
        model=Imgmodel
        fields='__all__'
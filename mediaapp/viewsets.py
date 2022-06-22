from rest_framework import viewsets
from . import models
from . import serilizers

class GalleryViewset(viewsets.ModelViewSet):
    queryset=models.Imgmodel.objects.all()
    serializer_class=serilizers.GallerySerilizer
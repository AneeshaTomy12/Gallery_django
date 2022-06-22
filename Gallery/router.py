from mediaapp.viewsets import GalleryViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('gallery',GalleryViewset)
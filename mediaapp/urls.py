from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
        path('',views.ApiOverView),
    path('gallerylist/',views.gallerylist,name="gallerylist")
]
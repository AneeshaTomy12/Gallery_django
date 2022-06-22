from django.shortcuts import render
from .forms import ImageForm 
from mediaapp.models import Imgmodel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from mediaapp.serilizers import GallerySerilizer

def home(request):
    form=ImageForm()
    imgs=Imgmodel.objects.all()
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
    return render(request,'index.html',{'form':form,'img':imgs})

@api_view(['GET']) 
def ApiOverView(request):
    return Response('API calling')

@api_view(['GET'])
def gallerylist(request):
    emp=Imgmodel.objects.all()
    serilizer=GallerySerilizer(emp,many=True)
    return Response(serilizer.data)



    

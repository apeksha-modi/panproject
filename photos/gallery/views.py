from django.shortcuts import render
from .models import Image
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import JsonResponse

def index(request):
    return render(request,'index.html')



def uploadImage(request):
    pi = request.FILES['image']
    fs = FileSystemStorage()
    print("request handling...")
    fs.save(pi.name,pi)
    print(pi.name)
    return render(request,'index.html')



# Create your views here.



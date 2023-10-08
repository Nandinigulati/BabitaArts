from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'accounts/home.html')

def gallery(request):
    return render(request,'accounts/gallery.html')

def about(request):
    return render(request,'accounts/about.html')

def murals(request):
    return render(request,'accounts/murals.html')

def scultures(request):
    return render(request,'accounts/scultures.html')

def paintings(request):
    return render(request,'accounts/paintings.html')

def wallpaintings(request):
    return render(request,'accounts/wallpaintings.html')

def metal(request):
    return render(request,'accounts/metal.html')

def contact(request):
    return render(request,'accounts/contact.html')


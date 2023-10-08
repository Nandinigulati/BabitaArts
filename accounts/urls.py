from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('gallery/', views.gallery, name="gallery"),
    path('about/', views.about,name="about"),
    path('scultures/', views.scultures,name="scultures"),
    path('murals/', views.murals,name="murals"),
    path('paintings/', views.paintings,name="paintings"),
    path('wallpaintings/', views.wallpaintings,name="wallpaintings"),
    path('metal/', views.metal,name="metal"),
    path('contact/', views.contact,name="contact"),

]

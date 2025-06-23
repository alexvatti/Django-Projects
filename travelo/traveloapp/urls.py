from django.contrib import admin
from django.urls import path,include
from .views import show
from . import views

urlpatterns = [
    path("",show,name="home"),
    path('index.html',views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('travel_destination.html', views.travel_destination, name='travel_destination'),
    path('destination_details.html', views.destination_details, name='destination_details'),
    path('elements.html', views.elements, name='elements'),
    path('blog.html', views.blog, name='blog'),
    path('single-blog.html', views.single_blog, name='single_blog'),
    path('contact.html', views.contact, name='contact'),
]

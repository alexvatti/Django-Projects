
from django.urls import path,include
from .views import show_packages

urlpatterns = [

    path("",show_packages,name='home'),
]
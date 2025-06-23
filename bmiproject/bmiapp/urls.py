from django.urls import path
from .views import bmi_form
urlpatterns = [
    path('', bmi_form,name="home"),
    
]
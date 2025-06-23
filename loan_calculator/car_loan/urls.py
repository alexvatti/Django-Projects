from django.urls import path
from .views import car_loan_view

urlpatterns = [
    path('', car_loan_view, name='car_loan'),
]
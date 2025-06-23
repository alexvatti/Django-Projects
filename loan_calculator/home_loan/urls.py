from django.urls import path
from .views import home_loan_view

urlpatterns = [
    path('', home_loan_view, name='home_loan'),
]

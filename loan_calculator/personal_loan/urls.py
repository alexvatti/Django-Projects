from django.urls import path
from .views import personal_loan_view

urlpatterns = [
    path('', personal_loan_view, name='personal_loan'),
]
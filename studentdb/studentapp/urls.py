from django.urls import path
from .views import student_details,student_add_show_records

urlpatterns = [
    path('', student_details, name='home'),
    path('students/', student_add_show_records, name='student-records'),
]
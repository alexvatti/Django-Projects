from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def show_packages(request):
    return render(request, 'package.html')
from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def travel_destination(request):
    return render(request, 'travel_destination.html')

def destination_details(request):
    return render(request, 'destination_details.html')

def elements(request):
    return render(request, 'elements.html')

def blog(request):
    return render(request, 'blog.html')

def single_blog(request):
    return render(request, 'single-blog.html')

def contact(request):
    return render(request, 'contact.html')
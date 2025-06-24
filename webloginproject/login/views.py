from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    context = {}

    if request.method == "POST":
        action = request.POST.get("action")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if action == "login":
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                context["error"] = "Invalid credentials"

        elif action == "signup":
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password)
                context["message"] = "Signup successful. You can now login."
            else:
                context["error"] = "Username already exists"

    return render(request, "base.html", context)

def logout_view(request):
    logout(request)
    return redirect("home")

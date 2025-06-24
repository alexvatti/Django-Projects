from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def auth_page(request):
    context = {}

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'signup':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password)
                context['message'] = "Signup successful. Please login."
            else:
                context['error'] = "Username already exists."

        elif action == 'login':
            user = authenticate(
                request,
                username=request.POST.get('username'),
                password=request.POST.get('password')
            )
            if user:
                login(request, user)
                return redirect('main-page')
            else:
                context['error'] = "Invalid login credentials."

        elif action == 'logout':
            logout(request)
            return redirect('main-page')

    return render(request, 'main.html', context)

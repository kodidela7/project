from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            User = get_user_model()  # Get the custom user model
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Registration successful! Please log in.")
                return redirect('login')  # Redirect to the login page
            
    return render(request, 'register.html')


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to login success page
            return redirect('login_success')  # Redirect to the page that shows successful login
        else:
            messages.error(request, "Invalid credentials.")

    return render(request, 'login.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
   logout(request)
   return redirect('login')  # Redirect back to login page after logout


from django.shortcuts import render


def login_success_view(request):
    return render(request, 'login_success.html')
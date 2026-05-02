from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import random

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        email = request.POST.get("email")

        if not email:
            messages.error(request, "Email is required.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        if form.is_valid():
            user = form.save(commit=False)

            user.username = form.cleaned_data["username"]
            user.email = email
            user.save()

            messages.success(request, "Account created successfully.")
            return redirect("main")

        else:
            messages.error(request, form.errors)

    else:
        form = UserCreationForm()

    return render(request, "auth/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("main")

        messages.error(request, "Invalid username or password")

    return render(request, "auth/login.html")

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")
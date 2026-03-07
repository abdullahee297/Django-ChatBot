from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        email = request.POST.get("email")

        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        if form.is_valid():
            user = form.save(commit=False)
            user.email = email
            user.save() 
            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")
        else:
            messages.error(request, "Passwords do not match or invalid data.")

    else:
        form = UserCreationForm()

    return render(request, "auth/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check the username and password in the database
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("main") 
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "auth/login.html")
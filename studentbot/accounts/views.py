from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages  


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            print("USER SAVED:", user.username)
            return redirect('home')

        else:
            print(form.errors)

    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})

def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "auth/login.html")


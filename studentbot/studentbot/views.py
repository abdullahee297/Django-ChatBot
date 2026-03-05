from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")

def base(request):
    return render(request, "base.html")

@login_required
def main(request):
    return render(request, "main.html")
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")

def base(request):
    return render(request, "base.html")

@login_required
def main(request):
    return render(request, "main.html", {
        "username": request.user.username
    })




@csrf_exempt
def chat_api(request):

    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": message,
                "stream": False
            }
        )

        ai_reply = response.json()["response"]

        return JsonResponse({"reply": ai_reply})
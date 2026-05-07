import os
import json
from django.shortcuts import render
from django.http import StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# print("KEY:", os.getenv("GROQ_API_KEY"))

def home(request):
    return render(request, "home.html")


def base(request):
    return render(request, "base.html")


@login_required
def main(request):
    return render(request, "main.html", {
        "username": request.user.username
    })


def groq_stream(prompt):
    try:
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        for chunk in stream:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                yield delta.content

    except Exception as e:
        yield f"\n[API ERROR] {str(e)}"

@csrf_exempt
@login_required
def chatbot_stream(request):
    prompt = request.GET.get("prompt", "").strip()

    if not prompt:
        return StreamingHttpResponse("No prompt provided", content_type="text/plain")

    def generate():
        try:
            full_response = ""

            for chunk in groq_stream(prompt):
                full_response += chunk
                yield chunk

        except Exception as e:
            yield f"\nError: {str(e)}"

    return StreamingHttpResponse(generate(), content_type="text/plain")

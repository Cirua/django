from multiprocessing import context
from django.shortcuts import render

def home(request):
    context = {
        "home_page": "Home page",
        "user_name": "John Doe"
    }
    return render(request, "home.html", context)


def about(request):
    context = {
        "about_page": "About page",
        "is_admin": True
    }
    return render(request, "about.html", context)

def login(request):
    context = {
        "login_page": "Login page"
    }
    return render(request, "login.html", context)
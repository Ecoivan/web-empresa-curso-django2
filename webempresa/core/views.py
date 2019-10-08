from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Este es el HOME</h1>")


def about(request):
    return HttpResponse("<h1>Este es el ABOUT</h1>")


def services(request):
    return HttpResponse("<h1>Este es el SERVICES</h1>")


def store(request):
    return HttpResponse("<h1>Este es el STORE</h1>")


def contact(request):
    return HttpResponse("<h1>Este es el CONTACT</h1>")


def blog(request):
    return HttpResponse("<h1>Este es el BLOG</h1>")


def sample(request):
    return HttpResponse("<h1>Este es el SAMPLE</h1>")

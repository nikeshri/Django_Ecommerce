from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    
    return render(request, "index.html")

def main(request):

    return render(request, "main.html")
def cart(request):

    return render(request, "cart.html")

def login(request):

    return render(request, "login.html")


def blogs(request):

    return render(request, "blogs.html")
def contact(request):

    return render(request, "contact.html")


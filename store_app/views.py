from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    
    return render(request, "index.html")

def login_page(request):

    return render(request, "login.html")

def login(request):
    
    return redirect('/login')

def register_page(request):

    return render(request, "register.html")

def register(request):

    return redirect('/register')

def category(request, id):

    return render(request, "category.html")
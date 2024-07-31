from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def menu(request):
    return render(request, 'home/menu.html')

def contact(request):
    return render(request, 'home/contact.html')

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "clenove\index.html")

def seznam(request):
    return render(request, "clenove\seznam.html")

def detail(request, prezdivka):
    return render(request, "clenove\detail.html")
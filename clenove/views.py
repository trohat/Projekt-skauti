from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Skaut

def index(request):
    return render(request, "clenove\index.html")

def seznam(request):
    skauti = Skaut.objects.all()
    return render(request, "clenove\seznam.html", {
        "skauti": skauti
    })

def detail(request, jmeno):
    skaut = get_object_or_404(Skaut, jmeno=jmeno)
    return render(request, "clenove\detail.html", {
        "skaut": skaut
    })
from django.shortcuts import render
from .models import Video

def home(request):
    context = {}
    return render(request, 'store/home.html', context)


def store(request):
    video=Video.objects.all()
    return render(request, 'store/store.html', {'video':video})


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def aboutUs(request):
    context = {}
    return render(request, 'store/aboutUs.html', context)

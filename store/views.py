from django.shortcuts import render

def store (request):
    context = {}
    return render (request, 'store/store.html', context )

def Cart (request):
    context = {}
    return render (request, 'store/Cart.html', context )

def checkout (request):
    context = {}
    return render (request, 'store/checkout.html', context )


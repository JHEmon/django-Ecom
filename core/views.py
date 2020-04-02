from django.shortcuts import render
from .models import Item
# Create your views here.

def item_list(requset):
    context = {
        'items': Item.objects.all
    }
    return render(requset, "home.html", context)

def CheckoutView(request):
    return render(request, "checkout.html")

def ProductsView(request):
    return render(request, "products.html")
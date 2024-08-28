from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.


def index(request):
    items = Item.objects.all()
    return render(request , "food/index.html" , {
        "items": items
    })


def item_detail(request , item_id):
    item = Item.objects.get(id = item_id)
    return render(request , "food/item_detail.html" , {
        "item" :  item
    })
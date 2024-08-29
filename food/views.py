from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def index(request):
    items = Item.objects.all()
    return render(request, "food/index.html", {
        "items": items
    })


def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, "food/item_detail.html", {
        "item":  item
    })


def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food_index')
    return render(request, 'food/add_item.html', {
        'form': form,
        
    })


def update_item(request , item_id):
    item = Item.objects.get(id = item_id)
    form = ItemForm(request.POST or None , instance=item)
    if(form.is_valid()):
        form.save()
        return redirect('food_index')
    return render(request , 'food/add_item.html', {
        'form' : form,
        # 'item' : item
    })


def delete_item(request : HttpRequest , item_id):
    item = Item.objects.get(id = item_id) 
    if request.method == 'POST':
        item.delete()
        return redirect('food_index')
    return render(request , 'food/delete_item.html', {
        'item' : item
    })
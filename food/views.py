from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import  reverse_lazy
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView

# Create your views here.

# Function-Based View
# def index(request):
#     items = Item.objects.all()
#     return render(request, "food/index.html", {
#         "items": items
#     })

class IndexView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = "items"


# def item_detail(request, item_id):
#     item = Item.objects.get(id=item_id)
#     return render(request, "food/item_detail.html", {
#         "item":  item
#     })

class ItemDetailView(DetailView):
    model = Item
    template_name = "food/item_detail.html"

# def add_item(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('food_index')
#     return render(request, 'food/add_item.html', {
#         'form': form,
        
#     })

class CreateItemView(CreateView):
    model = Item
    # form_class = ItemForm
    template_name = "food/add_item.html"
    success_url = reverse_lazy('food_index')
    fields = ['name' , 'desc' , 'price' , 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    


# def update_item(request , item_id):
#     item = Item.objects.get(id = item_id)
#     form = ItemForm(request.POST or None , instance=item)
#     if(form.is_valid()):
#         form.save()
#         return redirect('food_index')
#     return render(request , 'food/add_item.html', {
#         'form' : form,
#         # 'item' : item
#     })

class UpdateItemView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "food/add_item.html"
    success_url = reverse_lazy('food_index')


# def delete_item(request : HttpRequest , item_id):
#     item = Item.objects.get(id = item_id) 
#     if request.method == 'POST':
#         item.delete()
#         return redirect('food_index')
#     return render(request , 'food/delete_item.html', {
#         'item' : item
#     })

class DeleteItemView(DeleteView):
    model = Item
    template_name = 'food/delete_item.html'
    success_url =  reverse_lazy('food_index')

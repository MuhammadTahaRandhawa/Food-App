from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='food_index'),
    path('<int:item_id>', views.item_detail, name="food_item_detail"),
    path('additem/' , views.add_item , name="food_add_item"),
    path('updateitem/<int:item_id>', views.update_item , name =  'food_update_item'),
    path('deleteitem/<int:item_id>' , views.delete_item , name = "food_delete_item")
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='food_index'),
    path('<int:item_id>', views.item_detail, name="food_item_detail")
]

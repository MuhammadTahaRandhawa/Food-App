from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='food_index'),
    path('<int:pk>', views.ItemDetailView.as_view(), name="food_item_detail"),
    path('additem/', views.CreateItemView.as_view(), name="food_add_item"),
    path('updateitem/<int:pk>', views.UpdateItemView.as_view(),
         name='food_update_item'),
    path('deleteitem/<int:pk>', views.DeleteItemView.as_view(),
         name="food_delete_item")
]

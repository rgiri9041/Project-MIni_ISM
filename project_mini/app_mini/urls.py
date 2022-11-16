from django.urls import path
from .import views

urlpatterns = [
    path('items/', views.item_index, name="items.index"),
    path('items/create/', views.item_create, name="items.create"),
    path('items/edit/<int:id>/', views.item_edit, name="items.edit"),
    path('items/show/<int:id>/', views.item_show, name="items.show"),
    path('items/delete/<int:id>/', views.item_delete, name="items.delete"),
]
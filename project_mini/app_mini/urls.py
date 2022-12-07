from django.urls import path
from . import views 
from .views import(ItemApiView, ItemApiIDView)

urlpatterns = [
    #User
    path('user/login/', views.user_login, name="users.login"),
    path('user/logout/',  views.user_logout,name="users.logout"),
    path('user/register/', views.user_register, name="users.register"),
    path('user/profile/', views.user_profile, name="users.profile"),

    #items
    path('items/', views.item_index, name="items.index"),
    path('items/create/', views.item_create, name="items.create"),
    path('items/update/', views.item_update, name="items.update"),
    path('items/edit/<int:id>/', views.item_edit, name="items.edit"),
    path('items/show/<int:id>/', views.item_show, name="items.show"),
    path('items/delete/<int:id>/', views.item_delete, name="items.delete"),

    # api urls
    path('path/items/', ItemApiView.as_view()),
    path('path/items/<int:id>/', ItemApiIDView.as_view()),

]


    

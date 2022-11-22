from django.contrib import admin
from .models import Category, Item, AppUser
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
     
    list_dosplay = ("id", "category",)
    

class ItemAdmin(admin.ModelAdmin):
    list_distplay = ("title", "particular", "ledger_folio", "quantity", "price", "total", "entry_date" )
    list_filter = ('title', 'price')
   # search_fields: ("title")
class AppUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "middle_name", "last_name", "email", "password")


admin.site.register(Category, CategoryAdmin)
admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Item,ItemAdmin)

admin.site.site_title = "MINI_IMS"
admin.site.index_titel  = "Dashboard"
admin.site.site_header = "MINI IMS/Admin"
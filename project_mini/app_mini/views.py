from django.shortcuts import render, redirect
from .forms import ItemCreateForm
from .models import Category, Item, AppUser
from datetime import datetime
# Create your views here.
def item_index(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, 'items/index.html', context)

def item_create(request):
    item_create_form = ItemCreateForm()
    context = {"form": item_create_form}
    if request.method == "POST":
        context.update({"msg":"Item added successfully"})
        item = Item()
        category = Category.objects.get(id=request.POST.get('category'))
        item.title = request.POST.get('title')
        item.particular = request.POST.get('particular')
        item.ledger_folio = request.POST.get('ledger_folio')
        item.quantity = request.POST.get('quantity')
        item.price = request.POST.get('price')
        item.category_id = category.id
        item.total = float(item.price)*float(item.quantity)
        item.entry_date = datetime.now()
        item.save()
        return render(request, 'items/create.html', context)
    return render(request, 'items/create.html', context)

def item_edit(request, id):
    item = Item.objects.get(id=id)
    Categories = Category.objects.all()

    context = {"item": item,"categories": Categories}
    return render(request, 'items/edit.html', context)

def iitem_update(request):
    item_create_form = ItemCreateForm()
    context = {"form": item_create_form}
    if request.method == "POST":
        context.update({"msg":"Item added successfully"})
        item = Item(id=request.post.get('id'))

        category = Category.objects.get(id=request.POST.get('category'))
        item.title = request.POST.get('title')
        item.particular = request.POST.get('particular')
        item.ledger_folio = request.POST.get('ledger_folio')
        item.quantity = request.POST.get('quantity')
        item.price = request.POST.get('price')
        item.category_id = category.id
        item.total = float(item.price)*float(item.quantity)
        item.update_date = datetime.now()
        item.save()
        return redirect("items.index")
    return render(request, 'items/create.html', context)

def item_show(request, id):
    item = Item.objects.get(id=id)
    context = {"item": item}
    return render(request, 'items/show.html', context)

def item_delete(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect('items.index')
from django.shortcuts import render, redirect
from .forms import ItemCreateForm, UserLoginForm, UserRegistrationForm
from .models import Category, Item, AppUser
from datetime import datetime
# Create your views here.
def item_index(request):
    if request.session.has_key('session_user'):
        items = Item.objects.all()
        context = {"items": items}
        return render(request, 'items/index.html', context)
    return redirect("users.login")

def item_create(request):
    if request.session.has_key('session_user'):
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
    return redirect("users.login")

def item_edit(request, id):
    if request.session.has_key('session_user'):
        item = Item.objects.get(id=id)
        Categories = Category.objects.all()

        context = {"item": item,"categories": Categories}
        return render(request, 'items/edit.html', context)
    return redirect("users.login")

def iitem_update(request):
    if request.session.has_key('session_user'):
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
    return redirect("users.login")
    
def item_show(request, id):
    if request.session.has_key('session_user'):
        item = Item.objects.get(id=id)
        context = {"item": item}
        return render(request, 'items/show.html', context)
    return redirect("users.login")

def item_delete(request, id):
    if request.session.has_key('session_user'):
        item = Item.objects.get(id=id)
        item.delete()
        return redirect('items.index')
    return redirect("users.login")

def user_login(request):
    
    user_login_form = UserLoginForm()
    context = {"form":user_login_form}
    if request.method == "post":
         req_email = request.post.get('email')
         req_password = request.post.get('password')
         try:
            user = AppUser.objects.get(email=req_email)
            if user.email == req_email and user.password == req_password:
                request.session['session_email'] = user
                if request.session.has_key('session_user'):
                    return redirect("items.index")
                return redirect("users.login")
               
         except:
            return redirect("users.login")
    return render(request, "users/login.html",context)
     
def user_logout(request):
    if request.session.hs_key('session_user'):
        del request.session['session_user']
        return redirect("users_login")
    return redirect("users.login")

    
def user_register(request):
    user_register_form = UserRegistrationForm()
    context = {"form": user_register_form}
    if request.method == "post":
        user =  UserRegistrationForm(request.post)
        if user.is_valid:
            user.save()
            return redirect("users.register")
    return render(request, "users/register.html", context)
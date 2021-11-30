from django.shortcuts import render, redirect
from .models import Category, Product, Order, Customer
from .forms import OrderForms, CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


# Create your views here.


def index(request):
    # sql = select * from categories

    # orm -> object relational mapping

    categories = Category.objects.all()

    context = {
        "categories": categories,
    }

    return render(request, "index.html", context=context)

def user_registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form =  CreateUserForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/')
    context = {
        'form':form,
    }
    return render(request, 'register.html', context=context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, "user name or password is incorrect")    

    context = {}
    return render(request, 'login.html', context=context)   

def logout_user(request):
    logout(request)
    return redirect('login')         



def show_category(request, pk):
    category = Category.objects.get(id=pk)

    context = {
        "category": category,
    }
    return render(request, "category_details.html", context=context)


def about(request):
    return render(request, "about.html")


def order(request):
    form = OrderForms()

    if request.method == "POST":
        form = OrderForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order-list')

    context = {
        "form": form,
    }
    return render(request, "order.html", context=context)


def order_list(request):
    order_lists = Order.objects.all()

    context = {
        'orders': order_lists
    }

    return render(request, "orderlist.html", context=context)

def update_order(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForms(instance=order)

    if request.method == 'POST':
        form = OrderForms(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order-list')

    context = {
        'form': form
    }   
    return render(request, 'order.html', context=context)   

def show_order(request, pk):
    order_details = Order.objects.get(id=pk)

    context = {
        'order': order_details,
    }      
    return render(request, 'order_details.html', context=context) 

def delete_order(request, pk):
    item = Order.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('order-list')

    context = {
        'item': item,
    }

    return render(request, 'delete.html', context=context)    

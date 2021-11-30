from django.contrib import admin
from .models import Category, Customer, Product, Order

#admin view custom
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    search_fields = ['category_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'category_id', 'product_quantity'] 
    search_fields = ['product_name']
    filter=['product_price']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    search_fields = ['email', 'phone']
    filter = ['phone']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'product_id', 'quantity', 'delivery']        

# Register your models here.
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Customer, CustomerAdmin) 
admin.site.register(Product, ProductAdmin) 
admin.site.register(Order, OrderAdmin) 
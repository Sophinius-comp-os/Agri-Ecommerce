from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Address, Category, Order, OrderItem, Payment, Product, User

admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Product)

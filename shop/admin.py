from django.contrib import admin
from .models import Product, Category, Sales
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity',
                    'updated_at', 'created_at', 'category']
    list_filter = ['created_at', 'updated_at', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['product', 'paid_at',
                    'amount_paid', 'amount_given', 'quantity_bought']
    list_filter = ['paid_at']
    date_hierarchy = 'paid_at'

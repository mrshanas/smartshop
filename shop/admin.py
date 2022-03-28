from django.contrib import admin
from .models import Product, Category, Sales
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity',
                    'updated_at', 'created_at', 'category', 'shop_owner']
    list_filter = ['created_at', 'updated_at', 'category', 'shop_owner']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'shop_owner']
    list_filter = ['shop_owner', ]


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['product', 'paid_at',
                    'amount_paid', 'amount_given', 'shop_owner', 'quantity_bought', 'income']
    list_filter = ['paid_at', 'shop_owner']
    date_hierarchy = 'paid_at'

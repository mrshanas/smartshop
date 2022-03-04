from django import forms
from .models import Product, Category, Sales


class ProductForm(forms.ModelForm):
    """Register new products"""
    class Meta:
        model = Product
        exclude = ('shop_owner',)


class CategoryForm(forms.ModelForm):
    """Register new products"""
    class Meta:
        model = Category
        exclude = ('shop_owner',)


class SalesForm(forms.ModelForm):
    """Sell Products"""
    class Meta:
        model = Sales
        exclude = ('amount_given',)

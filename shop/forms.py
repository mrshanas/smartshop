from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """Register new products"""
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    """Register new products"""
    class Meta:
        model = Category
        fields = '__all__'

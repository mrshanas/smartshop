from django import forms
from .models import Product, Category, Sales


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


class SalesForm(forms.ModelForm):
    """Sell Products"""
    class Meta:
        model = Sales
        exclude = ('amount_given',)

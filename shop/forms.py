from django import forms
from .models import Product, Category, Sales
from django.contrib.auth import get_user_model


class ProductForm(forms.ModelForm):
    """Register new products"""
    class Meta:
        model = Product
        exclude = ('shop_owner', 'category')


class CategoryForm(forms.ModelForm):
    """Register new products"""
    class Meta:
        model = Category
        exclude = ('shop_owner',)


class SalesForm(forms.ModelForm):
    """Sell Products"""
    class Meta:
        model = Sales
        exclude = ('amount_given', 'shop_owner', 'product', 'income')


# class SearchForm(forms.Form):
#     """Search queries for product only"""
#     search = forms.CharField(max_length=200, required=True)

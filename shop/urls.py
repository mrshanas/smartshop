from django.urls import path
from .views import (ProductListView, CategoryListView,
                    SalesListView, ProductCreateView, SellProductView)
from . import views

app_name = 'shop'

urlpatterns = [
    # products url
    path('', views.home, name='home'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product/add/', ProductCreateView.as_view(), name='register_product'),
    path('product/<int:product_id>/edit/',
         views.edit_product, name='edit_product'),
    path('product/<int:product_id>/delete/',
         views.delete_product, name='delete_product'),

    # categories url
    path('categories', CategoryListView.as_view(), name='categories'),
    path('category/add/', views.register_category, name='register_category'),
    path('category/<int:category_id>/edit',
         views.edit_category, name='edit_category'),
    path('category/<int:category_id>/delete',
         views.delete_category, name='delete_category'),

    # sales url
    path('sales/', SalesListView.as_view(), name='sales'),
    path('sales/sell/', SellProductView.as_view(), name='sell'),

    # generate receipt
    path('sales/receipt/<int:sale_id>/', views.generate_receipt, name='receipt'),

    # search url
    # path('product/search', views.search_product, name='search')
]

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import CategoryForm, ProductForm, SalesForm
from .models import Category, Product, Sales


# product views

def home(request):
    """Display only 5 products"""
    queryset = Product.objects.all()[:5]

    return render(request, 'base.html', {'products': queryset})


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/products/products.html'
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/products/product.html'
    pk_url_kwarg = 'product_id'


def register_product(request):
    """Register new product in the db"""
    if request.method != 'POST':
        form = ProductForm()

    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:home')
    return render(request, 'shop/products/add_product.html', {'form': form})


def edit_product(request, product_id):
    """Edit the selected product"""
    product = get_object_or_404(Product, id=product_id)

    if request.method != 'POST':
        form = ProductForm(instance=product)
    else:
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:home')

    return render(request, 'shop/products/edit_product.html', {'form': form})


def delete_product(request, product_id):
    """Delete the selected product"""
    deleted_product = Product.objects.get(id=product_id).delete()
    print(deleted_product)
    return redirect('shop:home')

# category views


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'shop/categories/categories.html'


def register_category(request):
    """Register new category in the db"""
    if request.method != 'POST':
        form = CategoryForm()

    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:home')
    return render(request, 'shop/categories/add_category.html', {'form': form})


def edit_category(request, category_id):
    """Edit the selected category"""
    category = get_object_or_404(Category, id=category_id)
    if request.method != "POST":
        form = CategoryForm(instance=category)
    else:
        form = CategoryForm(data=request.GET, instance=category)
        if form.is_valid():
            form.save()
            return redirect('shop:categories')

    return render(request, 'shop/categories/edit_category.html', {'form': form})


def delete_category(request, category_id):
    """Delete the selected category"""
    deleted_product = Category.objects.get(id=category_id).delete()
    print(deleted_product)
    return redirect('shop:categories')

# sales views


class SalesListView(ListView):
    template_name = 'shop/sales/sales.html'
    context_object_name = 'sales'
    paginate_by = 10
    model = Sales


def sell_product(request):
    """Sell a new product"""
    if request.method != 'POST':
        form = SalesForm()
    else:
        form = SalesForm(data=request.POST)

        if form.is_valid():
            product = Product.objects.get(
                id=int(form.cleaned_data['product'].id)
            )
            sale = form.save(commit=False)
            sale_price = float(sale.quantity_bought) * float(product.price)
            product.quantity -= int(sale.quantity_bought)
            sale.amount_given = float(sale.amount_paid) - sale_price
            product.save()
            form.save()
            return redirect('shop:sales')

    return render(request, 'shop/sales/sell.html', {'form': form})

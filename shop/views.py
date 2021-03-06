from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.db.models import Sum
from django.template.loader import render_to_string

from .forms import CategoryForm, ProductForm, SalesForm
from .models import Category, Product, Sales

from weasyprint import HTML


# product views
@login_required
def home(request):
    """Display only 5 categories and search form"""

    queryset = Category.objects.filter(shop_owner=request.user)
    total_sales = Sales.objects.filter(
        shop_owner=request.user).aggregate(Sum('income'))
    products = Product.objects.all().filter(shop_owner=request.user)
    # if 'search' in request.GET:
    #     redirect('shop:search')

    return render(request, 'base.html', {'categories': queryset, 'sales': total_sales['income__sum'], 'products': products, })


# def search_product(request):
#     """Search for a specific product"""
#     product = Product.objects.filter(
#         name__search=request.GET['search'], shop_owner=request.user)
#     # print(product)
#     return render(request, 'shop/products/search.html', {product: product})


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop/products/products.html'
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.filter(shop_owner=self.request.user)


class ProductCreateView(LoginRequiredMixin, FormView):
    form_class = ProductForm
    success_url = '/products/'
    template_name = 'shop/products/add_product.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(shop_owner=self.request.user)
        context['categories'] = categories
        return context

    def form_valid(self, form):
        category = Category.objects.get(
            shop_owner=self.request.user, id=int(self.request.POST['category']))
        product = form.save(commit=False)
        product.shop_owner = self.request.user
        product.category = category
        product.save()
        return super().form_valid(form)


@login_required
def edit_product(request, product_id):
    """Edit the selected product"""
    product = get_object_or_404(
        Product, id=product_id, shop_owner=request.user
    )
    categories = Category.objects.filter(shop_owner=request.user)

    if request.method != 'POST':
        form = ProductForm(instance=product)
    else:
        form = ProductForm(data=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:products')

    return render(request, 'shop/products/edit_product.html', {'form': form, 'categories': categories})


@login_required
def delete_product(request, product_id):
    """Delete the selected product"""
    deleted_product = Product.objects.get(
        id=product_id, shop_owner=request.user).delete()
    print(deleted_product)
    return redirect('shop:products')

# category views


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'shop/categories/categories.html'
    paginate_by = 10

    def get_queryset(self):
        return Category.objects.filter(shop_owner=self.request.user)


@login_required
def register_category(request):
    """Register new category in the db"""
    if request.method != 'POST':
        form = CategoryForm()

    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.shop_owner = request.user
            category.save()
            return redirect('shop:home')
    return render(request, 'shop/categories/add_category.html', {'form': form})


@login_required
def edit_category(request, category_id):
    """Edit the selected category"""
    category = get_object_or_404(
        Category, id=category_id, shop_owner=request.user
    )

    if category.shop_owner != request.user:
        raise Http404

    if request.method != "POST":
        form = CategoryForm(instance=category)
    else:
        form = CategoryForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('shop:categories')

    return render(request, 'shop/categories/edit_category.html', {'form': form})


@login_required
def delete_category(request, category_id):
    """Delete the selected category"""
    deleted_product = Category.objects.get(
        id=category_id, shop_owner=request.user
    ).delete()
    print(deleted_product)
    return redirect('shop:categories')

# sales views


class SalesListView(LoginRequiredMixin, ListView):
    template_name = 'shop/sales/sales.html'
    context_object_name = 'sales'
    paginate_by = 10
    model = Sales

    def get_queryset(self):
        return Sales.objects.filter(shop_owner=self.request.user)


class SellProductView(LoginRequiredMixin, FormView):
    form_class = SalesForm
    success_url = '/sales/'
    template_name = 'shop/sales/sell.html'
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(shop_owner=self.request.user)
        context['products'] = products
        return context

    def form_valid(self, form):
        product = Product.objects.get(
            id=int(self.request.POST['product']),
            shop_owner=self.request.user
        )
        sale = form.save(commit=False)
        sale_price = float(sale.quantity_bought) * float(product.price)
        product.quantity -= int(sale.quantity_bought)
        amount_given = float(sale.amount_paid) - sale_price
        # if a customer pays less than the actual price
        sale.amount_given = amount_given if amount_given >= 0 else 0
        sale.income = sale_price
        sale.shop_owner = self.request.user
        sale.product = product
        product.save()
        sale.save()
        return super().form_valid(form)

# TODO transactions pdf


@login_required
def generate_receipt(request, sale_id):
    """Generate receipt for each transaction"""
    sale = Sales.objects.get(id=sale_id, shop_owner=request.user)
    html_template = render_to_string('shop/pdf.html', {'sale': sale})
    pdf_file = HTML(string=html_template).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline;filename=sold_product_{sale_id}.pdf'
    return response

# TODO styling and responsivity
# TODO filter the sales according to period
# TODO implement the search product functionality

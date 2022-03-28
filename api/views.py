from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView

from api.serializers import CategorySerializer, ProductsSerializer, SalesSerializer
from shop.models import Category, Product, Sales


class ProductListAndCreateView(ListCreateAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        new_queryset = Product.objects.all().filter(
            shop_owner=self.request.user,
            category__shop_owner=self.request.user
        )
        return new_queryset

    def perform_create(self, serializer):
        return serializer.save(shop_owner=self.request.user)


class CategoryListAndCreateView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        new_qs = super().get_queryset().filter(shop_owner=self.request.user)
        return new_qs

    def perform_create(self, serializer):
        return serializer.save(shop_owner=self.request.user)


class SalesListAndCreateView(ListCreateAPIView):
    serializer_class = SalesSerializer
    queryset = Sales.objects.all()

    def get_queryset(self):
        new_qs = super().get_queryset().filter(shop_owner=self.request.user)
        return new_qs

    def perform_create(self, serializer):
        sale_data = serializer.validated_data
        product = get_object_or_404(
            Product, id=sale_data.get('product').id, shop_owner=self.request.user)
        sale_price = float(sale_data.get('quantity_bought')
                           ) * float(product.price)
        product.quantity -= int(sale_data.get('quantity_bought'))
        amnt_given = float(sale_data.get('amount_paid')) - sale_price
        # if a customer pays less than the actual price
        amount_given = amnt_given if amnt_given >= 0 else 0
        product.save()
        return serializer.save(shop_owner=self.request.user, product=product, income=sale_price, amount_given=amount_given)

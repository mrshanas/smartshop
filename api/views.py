from rest_framework.generics import ListCreateAPIView

from api.serializers import CategorySerializer, ProductsSerializer
from shop.models import Category, Product


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

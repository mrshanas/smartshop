from rest_framework import serializers
from shop.models import Product, Category, Sales


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all())

    # this is to override drf create form
    # filter dropdown according to user category
    def __init__(self, *args, **kwargs):
        super(ProductsSerializer, self).__init__(*args, **kwargs)
        user = self.context['request'].user
        self.fields['category'].queryset = Category.objects.filter(
            shop_owner=user)

    class Meta:
        fields = ['id', 'name', 'price', 'quantity', 'category', ]
        model = Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        exclude = ['shop_owner', 'amount_given', 'income']

from rest_framework import serializers
from product.models import Category, Product, Review


class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
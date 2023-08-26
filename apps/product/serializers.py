from rest_framework import serializers
from .models import Subimage, Image, Subcategory, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'image']
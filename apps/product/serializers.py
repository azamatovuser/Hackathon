from rest_framework import serializers
from .models import Image, Subcategory, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Subcategory
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'images', 'created_date']


class ProductDetailSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    subcategory = SubcategorySerializer()
    class Meta:
        model = Product
        fields = ['id', 'account', 'title', 'description', 'image', 'subcategory', 'price', 'is_accepted']


# My product list serializers
class MyProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'images', 'created_date']


class ProductCreateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        account_id = self.request.user
        validated_data.account.id = account_id
        return validated_data

    def validate(self, attrs):
        account = self.request.user
        role = account.role
        if int(role) != 2:
            raise ValidationError({
                'message': 'You dont have permission for this'
            })
        return attrs
from rest_framework import generics
from .models import Subimage, Image, Subcategory, Category, Product
from .serializers import CategorySerializer, SubcategorySerializer, ProductListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return qs.filter(category_id=category_id)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        city_id = self.kwargs.get('city_id')
        country_id = self.kwargs.get('country_id')
        price = self.kwargs.get('price')
        expensive = self.kwargs.get('expensive')
        cheap = self.kwargs.get('cheap')
        newest = self.kwargs.get('newest')
        category_id = self.kwargs.get('category_id')
        subcategory_id = self.kwargs.get('subcategory_id')
        return qs
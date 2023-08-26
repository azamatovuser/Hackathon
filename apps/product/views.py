from rest_framework import generics
from .models import Image, Subcategory, Category, Product
from .serializers import CategorySerializer, SubcategorySerializer, \
    ProductListSerializer, ProductDetailSerializer, SubcategoryListSerializer, \
    MyProductListSerializer, ProductCreateSerializer, ImageSerializer
from apps.account.permissions import IsOwnUserOrReadOnly
from django.db.models import Q


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategoryListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return qs.filter(category_id=category_id)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        q_filters = Q()
        price = self.kwargs.get('price')
        expensive = self.kwargs.get('expensive')
        cheap = self.kwargs.get('cheap')
        if price:
            q_filters &= Q(price=price)
        else:
            if expensive:
                qs = qs.order_by('-price')
            elif cheap:
                qs = qs.order_by('price')
        newest = self.kwargs.get('newest')
        if newest:
            qs = qs.order_by('-created_date')
        qs = qs.filter(q_filters)
        return qs


class ProductRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsOwnUserOrReadOnly, ]


class MyProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = MyProductListSerializer
    permission_classes = [IsOwnUserOrReadOnly, ]

    def get_queryset(self):
        qs = super().get_queryset()
        account_id = self.request.user.id
        if account_id:
            return qs.filter(account_id=account_id)
        return []


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer


class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
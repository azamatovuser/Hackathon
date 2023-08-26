from django.urls import path
from .views import CategoryListAPIView, SubcategoryListAPIView, \
    ProductListAPIView, ProductRUDAPIView, MyProductListCreateAPIView, \
    ProductCreateAPIView, ImageListCreateAPIView


urlpatterns = [
    path('category_list/', CategoryListAPIView.as_view()),
    path('category/<int:category_id>/subcategory_list/', SubcategoryListAPIView.as_view()),
    path('product_list/', ProductListAPIView.as_view()),
    path('product_create/', ProductCreateAPIView.as_view()),
    path('product/detail/<int:pk>/', ProductRUDAPIView.as_view()),
    path('myproduct_list/', MyProductListCreateAPIView.as_view()),
    path('image_create/', ImageListCreateAPIView.as_view()),
]
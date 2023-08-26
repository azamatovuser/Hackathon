from django.urls import path
from .views import CategoryListAPIView, SubcategoryListAPIView, ProductListAPIView


urlpatterns = [
    path('category_list/', CategoryListAPIView.as_view()),
    path('category/<int:category_id>/subcategory_list/', SubcategoryListAPIView.as_view()),
    path('product_list/', ProductListAPIView.as_view()),
]
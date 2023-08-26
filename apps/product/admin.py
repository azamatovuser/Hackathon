from django.contrib import admin
from .models import Product, Category, Subimage, Subcategory, Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_accepted')


admin.site.register(Image)
admin.site.register(Subimage)
admin.site.register(Category)
admin.site.register(Subcategory)
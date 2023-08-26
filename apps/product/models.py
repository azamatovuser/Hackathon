from django.db import models
from apps.account.models import Account


class Category(models.Model):
    title = models.CharField(max_length=221)


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)


class Subimage(models.Model):
    subimage = models.ImageField(upload_to='product/images')


class Image(models.Model):
    subimage = models.ManyToManyField(Subimage)
    image = models.ImageField(upload_to='product/images/')


class Product(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    description = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    is_accepted = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

from django.db import models
import os
import datetime
from django.contrib.auth.models import User

# Create your models here.
def get_categories_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%S')
    filename = "%s %s" % (nowTime, original_filename)
    return os.path.join('uploads/categories/', filename)

def get_products_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%S')
    filename = "%s %s" % (nowTime, original_filename)
    return os.path.join('uploads/products/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_categories_file_path, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default 1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keyword = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_products_file_path, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    small_description = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    tag = models.CharField(max_length=150, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default 1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keyword = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Services(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default 1=Hidden")
    created_at = models.DateTimeField(auto_now_add=True)

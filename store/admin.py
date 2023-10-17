from django.contrib import admin
from store.models import Category, Product, Services
from django.utils.html import format_html

# Register your models here.
class categoryTable(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:50px; height:50px"/>'.format(obj.image.url))

    list_display = ('name', 'image_tag', 'slug')

class productTable(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="width:50px; height:50px"/>'.format(obj.image.url))

    list_display = ('name', 'image_tag', 'slug')

class serviceTable(admin.ModelAdmin):
    list_display = ('name', 'slug', 'original_price')

admin.site.register(Category, categoryTable)

admin.site.register(Product, productTable)

admin.site.register(Services, serviceTable)
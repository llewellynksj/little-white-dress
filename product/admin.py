from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('price', 'category', 'sizes_avail',)
    search_fields = ['item_name', 'category', 'price']

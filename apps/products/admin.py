from django.contrib import admin

from .models import (Product, Category, ShoppingCart)

admin.site.register(Category)
admin.site.register(ShoppingCart)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    ordering = ('name', 'category__name')

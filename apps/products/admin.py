from django.contrib import admin

from .models import (Product, Category, ShoppingCart)

admin.site.register(Category)
admin.site.register(ShoppingCart)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'categories', 'price')
    list_filter = ('categories',)
    search_fields = ('name', 'categories__name')
    ordering = ('name', 'categories__name')

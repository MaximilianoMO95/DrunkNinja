from django.contrib import admin

from .models import (Product, Category)

admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'categories', 'price')
    list_filter = ('categories',)
    search_fields = ('name', 'categories__name')
    ordering = ('name', 'categories__name')

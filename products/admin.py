from django.contrib import admin
from .models import *


# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]  # ["surname", "first_name"]
    inlines = [ProductImageInline]

    class Meta:
        model = ProductImage


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]  # ["surname", "first_name"]

    class Meta:
        model = ProductImage


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)

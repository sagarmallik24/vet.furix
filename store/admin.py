from django.contrib import admin
from .models import Category, Product, ProductImage
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ['category_name','slug']


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product','image')
    # prepopulated_fields = {'slug':('product',)}



admin.site.register(Category, categoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
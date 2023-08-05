from django.contrib import admin
from products.models import Product, Category, Tag, SubCategory, Feature

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(Feature)

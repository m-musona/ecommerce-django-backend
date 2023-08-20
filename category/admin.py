from django.contrib import admin
from category.models import Category, ElectronicsSubCategory,FashionSubCategory,WatchesSubCategory,AppliancesSubCategory,SportsAndLeisureSubCategory

# Register your models here.

admin.site.register(Category)
admin.site.register(ElectronicsSubCategory)
admin.site.register(FashionSubCategory)
admin.site.register(WatchesSubCategory)
admin.site.register(AppliancesSubCategory)
admin.site.register(SportsAndLeisureSubCategory)
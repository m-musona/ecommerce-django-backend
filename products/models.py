import os
import uuid
from django.db import models

# Create your models here.

class ElectronicsSubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False
    )

    def __str__(self):
        return self.id

class FashionSubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False
    )

    def __str__(self):
        return self.id
    

class SportsAndLeisureSubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False
    )

    def __str__(self):
        return self.id
    

class WatchesSubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False
    )

    def __str__(self):
        return self.id


class AppliancesSubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False
    )

    def __str__(self):
        return self.id

class Category(models.Model):
    id = models.CharField(max_length=50, blank=False, primary_key=True)
    electronics_sub_category = models.ManyToManyField(ElectronicsSubCategory)
    fashion_sub_category = models.ManyToManyField(FashionSubCategory)
    watches_sub_category = models.ManyToManyField(WatchesSubCategory)
    sports_and_leisure_sub_category = models.ManyToManyField(SportsAndLeisureSubCategory)
    appliances_sub_category = models.ManyToManyField(AppliancesSubCategory)

    def __str__(self):
        return self.id


def product_image_upload(instance, filename):
    # Upload the image to a directory named after the product's id
    return os.path.join("products", str(instance.id), filename)


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    product_image = models.ImageField(
        null=True,
        blank=True,
        width_field="product_image_width",
        height_field="product_image_height",
        upload_to="products/",
    )
    product_image_width = models.PositiveIntegerField(default=553)
    product_image_height = models.PositiveIntegerField(default=400)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=1,
    )
    electronics_sub_category = models.ForeignKey(
        ElectronicsSubCategory,
        on_delete=models.CASCADE,
        default=1,
    )
    fashion_sub_category = models.ForeignKey(
        FashionSubCategory,
        on_delete=models.CASCADE,
        default=1,
    )
    watches_sub_category = models.ForeignKey(
        WatchesSubCategory,
        on_delete=models.CASCADE,
        default=1,
    )
    sports_and_leisure_sub_category = models.ForeignKey(
        SportsAndLeisureSubCategory,
        on_delete=models.CASCADE,
        default=1,
    )
    appliances_sub_category = models.ForeignKey(
        AppliancesSubCategory,
        on_delete=models.CASCADE,
        default=1,
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

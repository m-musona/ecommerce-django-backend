import os
import uuid
from django.db import models

# Create your models here.


class Feature(models.Model):
    id = models.CharField(primary_key=True, max_length=50, blank=False)

    def __str__(self):
        return self.id


class Tag(models.Model):
    id = models.CharField(primary_key=True, max_length=50, blank=False)

    def __str__(self):
        return self.id


class SubCategory(models.Model):
    id = models.CharField(
        primary_key=True, max_length=50, blank=False, default="No Sub Category"
    )
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.id


class Category(models.Model):
    id = models.CharField(max_length=50, blank=False, primary_key=True)
    sub_category = models.ManyToManyField(SubCategory)

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
    features = models.ManyToManyField(Feature)
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
    sub_category = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE,
        default=1,
    )
    tags = models.ManyToManyField(Tag)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

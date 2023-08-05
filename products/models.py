import uuid
from django.db import models

# Create your models here.


class Feature(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=50, blank=False, default="No Sub Category")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Category(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=50, blank=False)
    sub_category = models.ManyToManyField(SubCategory)

    def __str__(self):
        return self.title


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    features = models.ManyToManyField(Feature)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default=2,
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

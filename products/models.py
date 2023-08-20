import uuid
from django.db import models
from category.models import Category, ElectronicsSubCategory,  FashionSubCategory, WatchesSubCategory, SportsAndLeisureSubCategory, AppliancesSubCategory
from rating.models import Rating
# Create your models here.

def product_image_path(instance, filename):
    # Use the product's title as the filename
    # extension = filename.split('.')[-1]
    # filename = f"{instance.title}.{extension}"
    # Upload the product image to a folder named after the product's UUID
    return f"products/{instance.id}/{filename}"

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    title = models.CharField(max_length=150, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    product_image = models.ImageField(
        null=True,
        blank=True,
        width_field="product_image_width",
        height_field="product_image_height",
        upload_to=product_image_path,
    )
    product_image_width = models.PositiveIntegerField(default=553)
    product_image_height = models.PositiveIntegerField(default=400)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    electronics_sub_category = models.ForeignKey(
        ElectronicsSubCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    fashion_sub_category = models.ForeignKey(
        FashionSubCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    watches_sub_category = models.ForeignKey(
        WatchesSubCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    sports_and_leisure_sub_category = models.ForeignKey(
        SportsAndLeisureSubCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    appliances_sub_category = models.ForeignKey(
        AppliancesSubCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

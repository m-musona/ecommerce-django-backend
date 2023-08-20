from products.models import Product
from category.models import Category
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "price",
            "product_image",
            "rating",
            "category",
            "electronics_sub_category",
            "fashion_sub_category",
            "watches_sub_category",
            "sports_and_leisure_sub_category",
            "appliances_sub_category",
            "updated",
            "created",
        ]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "electronics_sub_category",
            "fashion_sub_category",
            "watches_sub_category",
            "sports_and_leisure_sub_category",
            "appliances_sub_category",
        ]

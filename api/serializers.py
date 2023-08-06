from products.models import Product, Category
from rest_framework.serializers import ModelSerializer


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "price",
            "product_image",
            "features",
            "category",
            "tags",
            "sub_category",
            "updated",
            "created",
        ]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "sub_category",
        ]

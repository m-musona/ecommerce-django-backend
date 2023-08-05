from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product, Category, SubCategory, Tag
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProduct(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def getProductsByCategory(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProductsBySubCategory(request, category_id, sub_category_id):
    category = Category.objects.get(id=category_id)
    sub_category = SubCategory.objects.get(id=sub_category_id)
    products = Product.objects.filter(sub_category=sub_category, category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getProductsByTag(request, category_id, sub_category_id, tag_id):
    category = Category.objects.get(id=category_id)
    sub_category = SubCategory.objects.get(id=sub_category_id)
    tag = Tag.objects.get(id=tag_id)
    products = Product.objects.filter(
        sub_category=sub_category, category=category, tags=tag
    )
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product, Category, ElectronicsSubCategory,FashionSubCategory,WatchesSubCategory,AppliancesSubCategory,SportsAndLeisureSubCategory
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
    if category == "Electronics":
        sub_category = ElectronicsSubCategory.objects.get(id=sub_category_id)
    elif category == "Fashion":
        sub_category = FashionSubCategory.objects.get(id=sub_category_id)
    elif category == "Watches":
        sub_category = WatchesSubCategory.objects.get(id=sub_category_id)
    elif category == "Sports & Leisure":
        sub_category = SportsAndLeisureSubCategory.objects.get(id=sub_category_id)
    else:
        sub_category = AppliancesSubCategory.objects.get(id=sub_category_id)
    products = Product.objects.filter(sub_category=sub_category, category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

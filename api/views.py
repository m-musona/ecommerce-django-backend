from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from category.models import  Category, ElectronicsSubCategory,FashionSubCategory,WatchesSubCategory,AppliancesSubCategory,SportsAndLeisureSubCategory
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.


@api_view(["GET"])
def getAllProducts(request):
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
    if category_id == "Electronics":
        electronics_sub_category = ElectronicsSubCategory.objects.get(id=sub_category_id)
        products = Product.objects.filter(
        electronics_sub_category=electronics_sub_category,
        category=category)
    elif category_id == "Fashion":
        fashion_sub_category = FashionSubCategory.objects.get(id=sub_category_id)
        products = Product.objects.filter( 
        fashion_sub_category=fashion_sub_category,
        category=category)
    elif category_id == "Watches":
        watches_sub_category = WatchesSubCategory.objects.get(id=sub_category_id)
        products = Product.objects.filter(
        watches_sub_category=watches_sub_category,
        category=category)
    elif category_id == "Sports & Leisure":
        sports_and_leisure_sub_category = SportsAndLeisureSubCategory.objects.get(id=sub_category_id)
        products = Product.objects.filter(
        sports_and_leisure_sub_category=sports_and_leisure_sub_category,
        category=category)
    else:
        appliances_sub_category = AppliancesSubCategory.objects.get(id=sub_category_id)
        products = Product.objects.filter(
        appliances_sub_category=appliances_sub_category,
        category=category)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchForProducts(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(title__icontains=query)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response("Please provide a valid search query.", status=status.HTTP_400_BAD_REQUEST)

from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path("products/", views.getAllProducts),
    path("products/<uuid:id>/", views.getProduct),
    path("products/<str:category_id>/", views.getProductsByCategory),
    path(
        "products/<str:category_id>/<str:sub_category_id>/",
        views.getProductsBySubCategory,
    ),
    path("categories/", views.getCategories),
    path('search/', views.searchForProducts),
]

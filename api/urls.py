from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path("products/", views.getProducts),
    path("products/<uuid:id>/", views.getProduct),
    path("products/<str:category_id>/", views.getProductsByCategory),
    path(
        "products/<str:category_id>/<str:sub_category_id>/",
        views.getProductsBySubCategory,
    ),
    path(
        "products/<str:category_id>/<str:sub_category_id>/<str:tag_id>/",
        views.getProductsByTag,
    ),
    path("categories/", views.getCategories),
]

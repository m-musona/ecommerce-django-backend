from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path("products/", views.getProducts),
    path("products/<uuid:id>/", views.getProduct),
    path("products/<uuid:category_id>/", views.getProductsByCategory),
    path(
        "products/<uuid:category_id>/<uuid:sub_category_id>/",
        views.getProductsBySubCategory,
    ),
    path(
        "products/<uuid:category_id>/<uuid:sub_category_id>/<uuid:tag_id>/",
        views.getProductsByTag,
    ),
    path("categories/", views.getCategories),
]

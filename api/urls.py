from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("products/", views.getAllProducts),
    path("products/<uuid:id>/", views.getProduct),
    path("products/<str:category_id>/", views.getProductsByCategory),
    path(
        "products/<str:category_id>/<str:sub_category_id>/",
        views.getProductsBySubCategory,
    ),
    path("categories/", views.getCategories),
    path("search/", views.searchForProducts),
    # Uer token routes
    path("token/", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

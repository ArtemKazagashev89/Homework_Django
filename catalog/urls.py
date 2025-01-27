from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (ContactTemplateView, HomeView, ProductCreateView, ProductDeleteView, ProductDetailView,
                           ProductListView, ProductUpdateView, UnpublishProductView, ProductsInCategoryView)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("contacts/", ContactTemplateView.as_view(), name="contacts"),
    path("", ProductListView.as_view(), name="products_list"),
    path("product_detail/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product_new/", ProductCreateView.as_view(), name="product_create"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_confirm_delete"),
    path(
        "product_published_status/<int:product_id>/", UnpublishProductView.as_view(), name="product_published_status"
    ),
    path('category/<int:category_id>/', ProductsInCategoryView.as_view(), name='products_in_category'),
]

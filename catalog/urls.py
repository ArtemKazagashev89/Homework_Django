from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactTemplateView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
    path('', ProductListView.as_view(), name='products_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

from django.shortcuts import render
from catalog.models import Product

from django.views.generic import ListView, DetailView, View, TemplateView


class HomeView(View):
    def get(self, request):
        return render(request, 'catalog/home.html')


class ContactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'






from django.shortcuts import render
from django.views import generic
from .models import Category, Product


def CategoryProducts(request, selected_cat):
    # Displays all products within the selected category
    category_products = Product.objects.filter(
        category__category_name=selected_cat)
    return render(
        request,
        'category_products.html',
        {'selected_cat': selected_cat, 'category_products': category_products})


class ProductList(generic.ListView):
    # Displays all products when 'all styles' is selected
    model = Product
    template_name = 'all_products.html'


class CategoryList(generic.ListView):
    # Displays the product categorys on the homepage
    model = Category
    template_name = 'index.html'

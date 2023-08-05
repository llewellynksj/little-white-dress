from django.shortcuts import render
from django.views import generic
from .models import Category, Product


class CategoryList(generic.ListView):
    # Displays the product categorys on the homepage
    model = Category
    template_name = 'index.html'

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category, Product


class ProductDetails(generic.DetailView):
    # Displays individual product details
    model = Product
    template_name = 'product_details.html'

    # Code adapted from Codemy 'Add Blog Posts to Django' tutorial:
    # https://bit.ly/3s2sUq4
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetails, self).get_context_data(*args, **kwargs)
        data = get_object_or_404(Product, id=self.kwargs['pk'])
        liked = False
        if data.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        return context


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

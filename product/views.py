from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category, Product
from recommendations.models import Recommendation
from django.http import HttpResponseRedirect
from django.urls import reverse


def CustomerFavourites(request, pk):
    """
    Adds liked products to customer record
    """
    product = get_object_or_404(Product, id=request.POST.get('product_id'))
    liked = False
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
        liked = False
    else:
        product.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('product_details', args=[str(pk)]))


class ProductDetails(generic.DetailView):
    """
    Displays individual product details
    """
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
    """
    Displays all products within the selected category
    """
    category_products = Product.objects.filter(
        category__category_name=selected_cat)
    return render(
        request,
        'category_products.html',
        {'selected_cat': selected_cat, 'category_products': category_products})


class ProductList(generic.ListView):
    """
    Displays all products when 'all styles' is selected
    """
    model = Product
    template_name = 'all_products.html'


def DisplayHomepage(request):
    """
    Displays Homepage
    Passes in all objects from Category model
    Passes in first
    """
    category_list = Category.objects.all()
    recommendation_list = Recommendation.objects.all()

    context = {
        'category_list': category_list,
        'recommendation_list': recommendation_list,
    }
    return render(request, 'index.html', context)

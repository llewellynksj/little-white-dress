from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.display_homepage,
        name='index'),
    path(
        'products/',
        views.ProductList.as_view(),
        name='products'),
    path(
        'category/<str:selected_cat>/',
        views.category_products,
        name='category'),
    path(
        'product/<int:pk>',
        views.ProductDetails.as_view(),
        name='product_details'),
    path(
        'like/<int:pk>',
        views.customer_favourites,
        name='customer_fav'),
]

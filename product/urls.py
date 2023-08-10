from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.CategoryList.as_view(),
        name='index'),
    path(
        'products/',
        views.ProductList.as_view(),
        name='products'),
    path(
        'category/<str:selected_cat>/',
        views.CategoryProducts,
        name='category'),
    path(
        'product/<int:pk>',
        views.ProductDetails.as_view(),
        name='product_details'),
    path(
        'like/<int:pk>',
        views.CustomerFavourites,
        name='customer_fav'),
    path(
        'about/',
        views.DisplayAbout,
        name='about'),
    path(
        'contact/',
        views.DisplayContact,
        name='contact'),
]

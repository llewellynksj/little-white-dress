from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryList.as_view(), name='index'),
    path('products/', views.ProductList.as_view(), name='products'),
    path(
        'category/<str:selected_cat>/', views.CategoryProducts, name='category'
        ),
]

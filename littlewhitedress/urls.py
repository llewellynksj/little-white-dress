from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('customers/', include('django.contrib.auth.urls')),
    path('customers/', include('customer.urls')),
    path('community/', include('recommendations.urls')),
]

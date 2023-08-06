from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.CustomerRegistration.as_view(), name='register'),
    path('settings/', views.AccountSettings.as_view(), name='settings'),
    path('password/', views.UpdatePassword.as_view(template_name='registration/update_password.html')),
    path('create_profile/', views.CreateNewProfile.as_view(), name='create_profile'),
    path('<int:pk>/profile/', views.CustomerProfile.as_view(), name='profile'),
    path('<int:pk>/update_profile/', views.UpdateCustomerProfile.as_view(), name='update_profile'),
    
]

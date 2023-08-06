from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('settings/', views.UserEditView.as_view(), name='settings'),
    path('password/', views.PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('<int:pk>/profile/', views.UserProfileView.as_view(), name='profile'),
    path('<int:pk>/update_profile/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('create_profile/', views.CreateProfileView.as_view(), name='create_profile'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.DisplayAbout, name='about'),
    path('contact_details/', views.DisplayContact, name='contact_details'),
]

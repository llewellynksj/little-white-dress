from django.urls import path
from . import views

urlpatterns = [
    path(
        'about/',
        views.display_about,
        name='about'),
    path(
        '',
        views.display_contact,
        name='contact_details'),
]

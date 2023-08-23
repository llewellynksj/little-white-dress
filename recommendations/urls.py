from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.DisplayCommunityPage,
        name='community'),
]

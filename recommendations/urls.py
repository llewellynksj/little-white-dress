from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.RecommendationList.as_view(),
        name='community'),
    path(
        '<int:pk>/my_recommendations/',
        views.MyRecommendationsList.as_view(),
        name='my_recommendations'),
    path(
        '<int:pk>/add_recommendations/',
        views.AddRecommendations.as_view(),
        name='add_recommendations'),
    path(
        '<int:pk>/edit_recommendation/',
        views.EditRecommendation.as_view(),
        name='edit_recommendation')
]

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Recommendation
from .forms import AddNewRecommendationForm


class EditRecommendation(generic.UpdateView):
    """
    Displays form for user to update thier recommendation
    """
    model = Recommendation
    template_name = 'edit_recommendation.html'
    fields = (
        'type_of_recommendation',
        'title',
        'location',
        'web_link',
        'summary',
        'posted_by',
    )

    def get_success_url(self) -> str:
        return reverse_lazy(
            'my_recommendations', kwargs={'pk': self.object.pk}
        )


class AddRecommendations(generic.CreateView):
    """
    Links to custom add recommendations form
    """
    model = Recommendation
    form_class = AddNewRecommendationForm
    template_name = 'add_recommendation.html'

    # Make the user id available to be able to be saved to the form
    # Code from Codemy 'Profile Account Creation - Django Blog #32' video:
    # https://bit.ly/44Ymcjg
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy(
            'my_recommendations', kwargs={'pk': self.object.pk}
        )


class MyRecommendationsList(generic.ListView):
    """
    Displays all recommendation posts by User
    """
    model = Recommendation
    template_name = 'my_recommendations.html'

    # code adapted from Codemy 'Create a Blog Profile Page' Video:
    # http://bit.ly/3OsUgy8:
    def get_context_data(self, *args, **kwargs):
        context = super(
            MyRecommendationsList, self).get_context_data(
                *args, **kwargs)
        user_recommendations = Recommendation.objects.filter(
            user=self.request.user
        )
        context['user_recommendations'] = user_recommendations
        return context


class RecommendationList(generic.ListView):
    """
    Displays all User recommendations
    """
    model = Recommendation
    template_name = 'community.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            RecommendationList, self).get_context_data(
                *args, **kwargs)
        all_recommendations = Recommendation.objects.all
        context['all_recommendations'] = all_recommendations
        return context

from django.shortcuts import render
from django.views import generic
from .models import ContactDetail
from django.urls import reverse


def DisplayAbout(request):
    """
    Displays the About Us page
    """
    return render(request, 'about.html')


def DisplayContact(request):
    details_list = ContactDetail.objects.all()

    context = {'details_list': details_list}

    return render(request, 'contact_details.html', context)

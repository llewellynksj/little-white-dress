from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import ContactDetail, Enquiry


def DisplayContact(request):
    details_list = ContactDetail.objects.all()

    if request.method == "POST":
        full_name = request.POST['fullName']
        email_address = request.POST['emailAddress']
        message = request.POST['message']
        return render(request, 'contact_details.html', {
            'details_list': details_list,
            'full_name': full_name,
        })
    else:
        return render(request, 'contact_details.html', {})


def DisplayAbout(request):
    """
    Displays the About Us page
    """
    return render(request, 'about.html')

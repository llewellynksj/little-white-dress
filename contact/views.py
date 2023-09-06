from django.shortcuts import render
from django.views import generic
from .models import ContactDetail, Enquiry
from django.contrib import messages


def DisplayContact(request):
    details_list = ContactDetail.objects.all()

    if request.method == "POST":
        full_name = request.POST['fullName']
        email_address = request.POST['emailAddress']
        message = request.POST['message']
        messages.success(request, ('Your message has been sent!'))
        return render(request, 'contact_details.html', {
            'details_list': details_list,
            'full_name': full_name,
        })
    else:
        return render(
            request, 'contact_details.html', {'details_list': details_list})


def DisplayAbout(request):
    """
    Displays the About Us page
    """
    return render(request, 'about.html')

from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import ContactDetail, Enquiry
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def DisplayContact(request):
    details_list = ContactDetail.objects.all()

    if request.method == "POST":
        full_name = request.POST['fullName']
        email_address = request.POST['emailAddress']
        message = request.POST['message']

        # send email
        # send_mail(
        #     'LWD Enquiry Received from ' + full_name,
        #     message + 'FROM' + full_name,
        #     email_address,
        #     ['llewellyn.ksj@gmail.com'],
        # )
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

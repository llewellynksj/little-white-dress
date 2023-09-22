from django.shortcuts import render
from django.views import generic
from .models import ContactDetail, Enquiry
from django.contrib import messages
from .forms import EnquiryForm
from django.core.mail import send_mail
import os
if os.path.isfile('env.py'):
    import env


def display_contact(request):
    """
    Displays the Contact page
    Pulls contact details from the ContactDetails model and
    displays on page
    Validates contact form and saves
    Sends email of contact form
    """
    SEND_MAIL_EMAIL = os.environ.get('SEND_MAIL_EMAIL')
    details_list = ContactDetail.objects.all()

    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            print('form was valid')
            form.save()
            messages.success(request, ('Your message has been sent!'))

            # Send enquiry form as email
            send_mail(
                'LWD Website Enquiry from ' + form.cleaned_data['full_name'],
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                [SEND_MAIL_EMAIL],
            )

    form = EnquiryForm()
    return render(
        request, 'contact_details.html', {
            'details_list': details_list, 'form': form})


def display_about(request):
    """
    Displays the About Us page
    """
    return render(request, 'about.html')

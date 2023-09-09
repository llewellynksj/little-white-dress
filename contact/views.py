from django.shortcuts import render
from django.views import generic
from .models import ContactDetail, Enquiry
from django.contrib import messages
from .forms import EnquiryForm


def DisplayContact(request):
    details_list = ContactDetail.objects.all()

    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your message has been sent!'))

    form = EnquiryForm()
    return render(
        request, 'contact_details.html', {
            'details_list': details_list, 'form': form})


def DisplayAbout(request):
    """
    Displays the About Us page
    """
    return render(request, 'about.html')

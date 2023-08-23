from django.shortcuts import render


def DisplayCommunityPage(request):
    return render(request, 'community.html', {})

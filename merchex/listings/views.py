from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Announcement


def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',
                  {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def contacts(request):
    return render(request, 'listings/contact.html')

def ads(request):
    announcements = Announcement.objects.all()
    return render(request, 'listings/ads.html',
                  {'announcements': announcements})

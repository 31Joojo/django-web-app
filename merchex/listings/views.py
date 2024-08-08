from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def home(request):
    return render(request, 'listings/base.html')

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html',
                  {'bands': bands})

def about(request):
    return render(request, 'listings/about.html')

def contacts(request):
    return render(request, 'listings/contact.html')

def ads(request):
    listings = Listing.objects.all()
    return render(request, 'listings/ads.html',
                  {'listings': listings})

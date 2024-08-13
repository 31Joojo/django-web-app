from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def home(request):
    return render(request, 'listings/base.html')

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html',
                  {'bands': bands})

def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
                  'listings/band_detail.html',
                  {'band_id': band_id, 'band': band})

def about(request):
    return render(request, 'listings/about.html')

def contacts(request):
    return render(request, 'listings/contact.html')

def ads(request):
    listings = Listing.objects.all()
    return render(request, 'listings/ad_list.html',
                  {'listings': listings})

def ad_detail(request, ad_id):
    ad = Listing.objects.get(id=ad_id)
    return render(request,
                  'listings/ad_detail.html',
                  {'ad_id': ad_id, 'ad': ad})

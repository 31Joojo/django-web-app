from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Announcement


def hello(request):
    bands = Band.objects.all()
    announcements = Announcement.objects.all()
    return render(request, 'listings/hello.html',
                  {'bands': bands})

def about(request):
    return HttpResponse('<h1>About us!</h1> <p>We love merch! </p>')

def contacts(request):
    return HttpResponse('<h1>Contact us</h1>')

def ads(request):
    return HttpResponse('<h1>Ads available</h1>')

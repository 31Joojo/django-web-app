from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1≥')

def about(request):
    return HttpResponse('<h1>About us!</h1> <p>We love merch! </p>')

def contacts(request):
    return HttpResponse('<h1>Contact us</h1>')

def ads(request) :
    return HttpResponse('<h1>Ads available</h1>')

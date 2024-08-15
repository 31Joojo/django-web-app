from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Band, Listing
from listings.forms import ContactForm, BandForm
from django.core.mail import send_mail


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

def band_create(request):
    band_form = BandForm()
    return render(request,
                  'listings/band_create.html',
                  {'band_form': band_form})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    print('La méthode requête est : ', request.method)
    print('Les données post sont :', request.POST)
    if request.method == 'POST':
        ## Crée une instance du formulaire et le remplit avec les données POST
        form = ContactForm(request.POST)

        ##
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via Merchex contact-us form.',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=["admin@merchex.xyz"],
            )
        return redirect('email-sent')
    else:
        ## Crée un nouveau formulaire vide
        form = ContactForm()
    return render(request,
                  'listings/contact.html',
                  {'form': form})

def ads(request):
    listings = Listing.objects.all()
    return render(request, 'listings/ad_list.html',
                  {'listings': listings})

def ad_detail(request, ad_id):
    ad = Listing.objects.get(id=ad_id)
    return render(request,
                  'listings/ad_detail.html',
                  {'ad_id': ad_id, 'ad': ad})

def confirmation(request):
    return render(request,
                  'listings/confirmation.html')

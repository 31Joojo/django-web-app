from django import forms

from listings.models import Band, Listing


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)

class BandForm(forms.ModelForm):
    ## Classe imbriquée qui définit quel modèle et quels champs du modèle à utiliser
    class Meta:
        model = Band
        ## fields = '__all__'
        exclude = ('active', 'official_homepage')

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ('sold',)

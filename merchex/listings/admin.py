from django.contrib import admin

from listings.models import Band, Listing

## Afficher le genre et l'année de formation de chaque groupe
class BandAdmin(admin.ModelAdmin):
    ## Liste des champs à afficher
    list_display = ('id', 'name', 'year_formed', 'genre')


admin.site.register(Band, BandAdmin)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'sold', 'type')


admin.site.register(Listing, ListingAdmin)

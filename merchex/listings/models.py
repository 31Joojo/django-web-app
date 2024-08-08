from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    ## Sous-classe pour répertorier les différents genres possibles
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        K_POP = 'KP'
        ZOUK = 'ZK'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
class Announcement(models.Model):
    ## Sous-classe pour répertorier les différents types
    class Type(models.TextChoices):
        RECORDS = 'RE'
        CLOTHING = 'CL'
        POSTERS = 'PO'
        MISCELLANEOUS = 'MI'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=300)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    type = models.fields.CharField(choices=Type.choices, max_length=5)

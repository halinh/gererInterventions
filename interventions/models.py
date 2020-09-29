from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Intervention(models.Model):
    libelle = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    nom_intervenant = models.CharField(max_length=70, blank=False, default='')
    lieu = models.CharField(max_length=70, blank=False, default='')
    date = models.DateField()
    featured = models.BooleanField(default=False)
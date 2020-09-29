from rest_framework import serializers
from .models import Intervention


class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervention
        fields = ('id',
                  'libelle',
                  'description',
                  'nom_intervenant',
                  'lieu',
                  'date',
                  'featured')
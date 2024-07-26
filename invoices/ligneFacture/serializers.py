from rest_framework import serializers
from .models import LigneFacture

class LigneFactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneFacture
        fields = ['facture', 'description', 'quantite', 'prix_unitaire', 'total_ligne', 'total_ligne_htva']

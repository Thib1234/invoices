# serializers.py
from rest_framework import serializers
from facturation.models import Facture
from ligneFacture.models import LigneFacture

class LigneFactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = LigneFacture
        fields = ['description', 'quantite', 'prix_unitaire', 'total_ligne', 'total_ligne_htva']

class FactureSerializer(serializers.ModelSerializer):
    lignes_facture = LigneFactureSerializer(many=True, read_only=True, source='lignefacture_set')

    class Meta:
        model = Facture
        fields = ['id', 'client', 'date', 'statut', 'montant_total', 'montant_tva', 'total_htva', 'send', 'lignes_facture']

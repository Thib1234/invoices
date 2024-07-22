from django.db import models
from facturation.models import Facture

# Create your models here.
class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=5, decimal_places=2)
    total_ligne = models.DecimalField(max_digits=5, decimal_places=2)
    total_ligne_htva = models.DecimalField(max_digits=5, decimal_places=2)
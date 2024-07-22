from django.db import models
from facturation.models import Facture

# Create your models here.
class Paiement(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    date = models.DateField()
    montant = models.DecimalField(max_digits=5, decimal_places=2)
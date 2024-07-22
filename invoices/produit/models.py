from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    prix_htva = models.DecimalField(max_digits=5, decimal_places=2)
    prix_achat = models.DecimalField(max_digits=5, decimal_places=2)
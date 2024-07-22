from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from client.models import Client


# Create your models here.
class Facture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    total = models.DecimalField(max_digits=5, decimal_places=2)
    statut = models.CharField(max_length=20)
    montant_total = models.DecimalField(max_digits=5, decimal_places=2)
    montant_tva = models.DecimalField(max_digits=5, decimal_places=2)
    send = models.BooleanField(default=False)

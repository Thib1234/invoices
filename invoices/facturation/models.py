from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from client.models import Client
import datetime
from django.conf import settings


# Create your models here.
class Facture(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    statut = models.CharField(max_length=20)
    montant_total = models.DecimalField(max_digits=15, decimal_places=2)
    total_htva = models.DecimalField(max_digits=15, decimal_places=2)
    montant_tva = models.DecimalField(max_digits=15, decimal_places=2)
    send = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # Nouveau champ


    @property
    def lignes_factures(self):
        return self.lignefacture_set.all()
    
    def __str__(self):
        return self.nom
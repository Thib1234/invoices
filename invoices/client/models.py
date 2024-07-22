from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    num_tva = models.CharField(max_length=20)
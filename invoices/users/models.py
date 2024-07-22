from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from client.models import Client


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_factures = models.IntegerField(default=0)


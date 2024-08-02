from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # autres champs
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    code_postal = models.CharField(max_length=10)
    ville = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    num_tva = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)  # Nouveau champ

    def __str__(self):
        return self.nom
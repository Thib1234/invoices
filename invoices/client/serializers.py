from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id','nom', 'adresse', 'code_postal', 'ville', 'email', 'telephone', 'num_tva']  # Ne pas inclure 'user'

    def create(self, validated_data):
        user = self.context['request'].user
        # Crée l'objet Client en utilisant les données validées sans 'user'
        return Client.objects.create(user=user, **validated_data)

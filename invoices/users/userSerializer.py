from rest_framework import serializers
from .models import CustomUser

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'nom_societe', 'num_bce', 'adresse', 'ville', 'code_postal', 'telephone']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

import json
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .userSerializer import UtilisateurSerializer

class UtilisateurViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            user = User(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email']
            )
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({"status": "Utilisateur créé avec succès"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login_view(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            # Récupérer l'utilisateur par email
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Invalid email or password'}, status=400)

            # Authentifier en utilisant le username de l'utilisateur
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return JsonResponse({'token': token})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid email or password'}, status=400)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

from rest_framework import viewsets
from .models import LigneFacture
from .serializers import LigneFactureSerializer
from rest_framework.permissions import IsAuthenticated

class LigneFactureViewSet(viewsets.ModelViewSet):
    queryset = LigneFacture.objects.all()
    serializer_class = LigneFactureSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(facture__user=self.request.user)

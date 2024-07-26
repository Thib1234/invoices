# views.py
from rest_framework import viewsets
from facturation.models import Facture
from facturation.serializers import FactureSerializer
from rest_framework.permissions import IsAuthenticated

class FactureViewSet(viewsets.ModelViewSet):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).prefetch_related('lignefacture_set')

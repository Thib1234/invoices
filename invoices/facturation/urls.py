from django.urls import path
from .views import FactureViewSet, generate_invoice_pdf

urlpatterns = [
    path('create/', FactureViewSet.as_view({'post': 'create'}), name='create'),
    path('list/', FactureViewSet.as_view({'get': 'list'}), name='list'),
    path('recent/', FactureViewSet.as_view({'get': 'recent'}), name='recent'),  # Nouvelle route
    path('generate-invoice/<int:facture_id>/', generate_invoice_pdf, name='generate_invoice'),
    path('total-amount-by-month/', FactureViewSet.as_view({'get': 'total_amount_by_month'}), name='total_amount_by_day'),
]

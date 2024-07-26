from django.urls import path
from .views import FactureViewSet

urlpatterns = [
    path('create/', FactureViewSet.as_view({'post': 'create'}), name='create'),
    path('list/', FactureViewSet.as_view({'get': 'list'}), name='list'),
    path('recent/', FactureViewSet.as_view({'get': 'recent'}), name='recent'),  # Nouvelle route
]

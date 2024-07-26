from django.urls import path
from .views import LigneFactureViewSet

urlpatterns = [
    path('create/', LigneFactureViewSet.as_view({'post': 'create'}), name='create'),
    path('list/', LigneFactureViewSet.as_view({'get': 'list'}), name='list'),
    path('recent/', LigneFactureViewSet.as_view({'get': 'recent'}), name='recent'),  # Nouvelle route
]

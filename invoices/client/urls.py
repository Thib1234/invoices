from django.urls import path
from .views import ClientViewSet

urlpatterns = [
    path('create/', ClientViewSet.as_view({'post': 'create'}), name='create'),
    path('list/', ClientViewSet.as_view({'get': 'list'}), name='list'),
    path('recent/', ClientViewSet.as_view({'get': 'recent'}), name='recent'),  # Nouvelle route
]

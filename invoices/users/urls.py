from django.urls import path
from .views import UtilisateurViewSet

urlpatterns = [
    path('register/', UtilisateurViewSet.as_view({'post': 'create'}), name='register'),
    path('login/', UtilisateurViewSet.as_view({'post': 'login_view'}), name='login'),
]

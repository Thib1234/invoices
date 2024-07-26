from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('client/', include('client.urls')),  # Inclure les URLs de ton application client
    path('invoice/', include('facturation.urls')),  # Inclure les URLs de ton application client
    path('lignefacture/', include('ligneFacture.urls')),  # Inclure les URLs de ton application client
    path('accounts/', include('users.urls')),
    # Ajoute ici les autres applications si nécessaire
]

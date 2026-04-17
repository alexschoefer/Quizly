from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationView, CookieTokenObtainPairView, TokenRefreshView, LogoutView, CustomTokenRefreshView

urlpatterns = [
    path('api/register/', RegistrationView.as_view(), name='registration'),
    path('api/login/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]

from rest_framework import status, generics
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegistrationView(generics.CreateAPIView):
    """
    API view for user registration.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"detail": "User created successfully!"}, status=status.HTTP_201_CREATED)

class CookieTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to obtain JWT tokens and set the refresh token in an HTTP-only cookie.
    """

    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """
        Override the post method to set the refresh token in an HTTP-only cookie and return user information in the response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        access = serializer.validated_data.get("access")
        refresh = serializer.validated_data.get("refresh")
        user = serializer.validated_data.get("user")

        response = self._create_login_response(user)

        response.set_cookie(
            key='access_token',
            value=str(access),
            httponly=True,
            secure=False,
            samesite='Lax'
        )

        response.set_cookie(
            key='refresh_token',
            value=str(refresh),
            httponly=True,
            secure=False,
            samesite='Lax'
        )
        
        return response

    def _create_login_response(self, user):
        """Create a response containing user information after successful login."""
        return Response({
            "detail": "Login successful!",
            "user": user
        }, status=status.HTTP_200_OK)
    
class LogoutView(APIView):
    """
    API view for user logout. This view deletes the JWT tokens from the cookies.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Override the post method to delete the JWT tokens from the cookies and blacklist the refresh token if it exists.
        """
        refresh = request.COOKIES.get("refresh_token")

        response = Response({"detail": "Logged out"}, status=200)

        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        if refresh:
            try:
                token = RefreshToken(refresh)
                token.blacklist()
            except:
                pass

        return response
    
class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom view to refresh JWT tokens and update the access token in an HTTP-only cookie.
    """

    def post(self, request, *args, **kwargs):
        """
        Override the post method to refresh the access token and set it in an HTTP-only cookie.
        """
        refresh_token = request.COOKIES.get('refresh_token')
        if refresh_token is None:
            return Response({"detail": "Refresh token not provided in cookies."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data={"refresh": refresh_token})

        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_401_UNAUTHORIZED)
        
        access_token = serializer.validated_data.get("access")

        response = Response({"detail": "Token refreshed successfully!"}, status=status.HTTP_200_OK)
        response.set_cookie(
            key='access_token',
            value=str(access_token),
            httponly=True,
            secure=False,
            samesite='Lax'
        )

        return response
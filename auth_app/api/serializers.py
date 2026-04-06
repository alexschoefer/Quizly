from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    confirmed_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirmed_password', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def save(self):
        """Create a new user instance after validating the data."""
        pw = self.validated_data['password']
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(pw)
        account.save()
        return account
        
    
    def validate(self, data):
        """
        Validate that the password and confirm_password fields match.
        """
        password = data.get('password')
        confirmed_password = data.get('confirmed_password')
        if password != confirmed_password:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    def validate_email(self, value):
        """
        Validate that the email is unique.
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value
    
    def validate_username(self, value):
        """
        Validate that the username is unique.
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already in use.")
        return value
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer for obtaining JWT tokens. 
    This can be extended to include additional user information in the token response.
    """
    def validate(self, attrs):
        """
        Validate the user credentials and return the token along with user information.
        """
        data = super().validate(attrs)
        data.update({'user': {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email
        }})

        return data

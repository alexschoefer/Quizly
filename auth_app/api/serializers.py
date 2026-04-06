from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        """"
        Create and return a new user instance, given the validated data.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
    
    def validate(self, data):
        """
        Validate that the password and confirm_password fields match.
        """
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
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
        data = super().validate(attrs)
        data.update({'user': {
            'user_id': self.user.id,
            'username': self.user.username,
            'email': self.user.email
        }})

        return data

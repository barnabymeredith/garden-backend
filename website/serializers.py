from rest_framework import serializers
from .models import Picture, Marker
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MarkerSerializer(serializers.ModelSerializer):

    name = serializers.CharField(allow_blank=True)
    description = serializers.CharField(allow_blank=True)
    top = serializers.FloatField()
    left = serializers.FloatField()
    picture = serializers

    class Meta:
        model = Marker
        fields = ['id', 'name', 'description', 'top', 'left']

class PictureSerializer(serializers.ModelSerializer):

    name = serializers.CharField(allow_blank=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Picture
        fields = ['name', 'user']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        token['email'] = user.email

        return token
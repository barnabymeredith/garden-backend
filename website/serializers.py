from rest_framework import serializers
from .models import Picture, Marker

class MarkerSerializer(serializers.ModelSerializer):

    name = serializers.CharField(allow_blank=True)
    description = serializers.CharField(allow_blank=True)
    top = serializers.FloatField()
    left = serializers.FloatField()

    class Meta:
        model = Marker
        fields = ['id', 'name', 'description', 'top', 'left']

class PictureSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(required=False)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Picture
        fields = ['image', 'user']
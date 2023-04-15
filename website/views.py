from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Marker, Picture
from .serializers import CustomTokenObtainPairSerializer, MarkerSerializer, PictureSerializer

from rest_framework import viewsets

from rest_framework_simplejwt.views import TokenObtainPairView

class MarkerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer

    def update(self, request, pk=None):
        try:
            marker = Marker.objects.get(pk=pk)
        except Marker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(marker, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
class PictureViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Marker  
from .serializers import MarkerSerializer

from rest_framework import viewsets

class MarkerViewSet(viewsets.ModelViewSet):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'markers', views.MarkerViewSet, 'marker')

urlpatterns = [
    path('api/', include(router.urls)),
]
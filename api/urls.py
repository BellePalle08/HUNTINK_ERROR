from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import TattooArtistViewSet, TattooViewSet

router = routers.DefaultRouter()
router.register('tattooartists', TattooArtistViewSet)
router.register('tattoos', TattooViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
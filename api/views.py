from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import TattooArtist, TattooArtistPhoto, TattooArtistStyle, Tattoo, TattooStyle, Review, Rating, Favourites
from .serializer import TattooArtistSerializer, TattooSerializer, ReviewSerializer, FavouritesSerializer, RatingSerializer, TattooStyleSerializer, TattooArtistStyleSerializer, TattooArtistPhotoSerializer

class TattooArtistViewSet(viewsets.ModelViewSet):
    queryset = TattooArtist.objects.all()
    serializer_class = TattooArtistSerializer

class TattooViewSet(viewsets.ModelViewSet):
    queryset = Tattoo.objects.all()
    serializer_class = TattooSerializer

class TattooArtistStyleViewSet(viewsets.ModelViewSet):
    queryset = TattooArtistStyle.objects.all()
    serializer_class = TattooArtistStyleSerializer

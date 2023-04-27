from rest_framework import serializers
from .models import TattooArtist, TattooArtistPhoto, TattooArtistStyle, Tattoo, TattooStyle, Review, Rating, Favourites
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only' : True, 'required' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class TattooArtistStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooArtistStyle
        fields = ('id', 'tattooArtist', 'stile')

class TattooArtistPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooArtistPhoto
        fields = ('id', 'tattooArtist', 'sfondo')


class TattooArtistSerializer(serializers.ModelSerializer):

    styles = serializers.SerializerMethodField()
    sfondi = serializers.SerializerMethodField()
    recensioni = serializers.SerializerMethodField()

    def get_styles(self, tattooArtist):
        qs = TattooArtistStyle.objects.filter(tattooArtist=tattooArtist)
        serializer = TattooArtistStyleSerializer(instance=qs, many=True)
        return serializer.data

    def get_sfondi(self, tattooArtist):
        qs = TattooArtistPhoto.objects.filter(tattooArtist=tattooArtist)
        serializer = TattooArtistPhotoSerializer(instance=qs, many=True)
        return serializer.data

    def get_recensioni(self, tattooArtist):
        qs = Review.objects.filter(tattooArtist=tattooArtist)
        serializer = ReviewSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = TattooArtist
        fields = ('id', 'nome', 'via', 'citta', 'provincia', 'cap', 'descrizione', 'email', 'telefono', 'no_of_ratings', 'avg_of_ratings', 'no_of_review', 'styles', 'sfondi', 'recensioni')

class TattooStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooStyle
        fields = ('id', 'tattoo', 'stile')

class TattooSerializer(serializers.ModelSerializer):
    styles = serializers.SerializerMethodField()

    def get_styles(self, tattoo):
        qs = TattooStyle.objects.filter(tattoo=tattoo)
        serializer = TattooStyleSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Tattoo
        fields = ('id', 'tattooArtist', 'foto', 'no_of_Favourites', 'styles')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'tattooArtist', 'user', 'testo', 'voto')

class FavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourites
        fields = ('id', 'user', 'tattoo')

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'TattooArtist', 'user', 'stars')


class TattooArtistStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooArtistStyle
        fields = ('id', 'tattooArtist', 'stile')

class TattooArtistPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooArtistPhoto
        fields = ('id', 'tattooArtist', 'sfondo')


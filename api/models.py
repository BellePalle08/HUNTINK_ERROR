from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.



class TattooArtist(models.Model):
    nome = models.CharField(max_length = 60, blank = False, unique = True)
    via = models.CharField(max_length = 60, blank = False)
    citta = models.CharField(max_length=60, blank=False)
    provincia = models.CharField(max_length=60, blank=False)
    cap = models.CharField(max_length=10, blank=False)
    descrizione = models.TextField(max_length=256, blank=True)
    email = models.CharField(max_length=80, blank=False)
    telefono = models.CharField(max_length=20, blank=False)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(tattooArtist=self)
        return len(ratings)

    def avg_of_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(tattooArtist=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    def no_of_review(self):
        review = Review.objects.filter(tattooArtist=self)
        return len(review)


class TattooArtistPhoto(models.Model):
    tattooArtist = models.ForeignKey(TattooArtist, on_delete=models.CASCADE, related_name="sfondi")
    sfondo = models.ImageField(upload_to='covers/', blank=False)

class TattooArtistStyle(models.Model):
    tattooArtist = models.ForeignKey(TattooArtist, on_delete=models.CASCADE)
    stile = models.CharField(max_length=30, blank=False)

class Tattoo(models.Model):
    tattooArtist = models.ForeignKey(TattooArtist, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='covers/', blank=False)

    def no_of_Favourites(self):
        favourites = Favourites.objects.filter(tattoo=self)
        return len(favourites)

class TattooStyle(models.Model):
    tattoo = models.ForeignKey(Tattoo, on_delete=models.CASCADE)
    stile = models.CharField(max_length=30, blank=False)

class Review(models.Model):
    tattooArtist = models.ForeignKey(TattooArtist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testo = models.TextField(max_length=256, blank=True)
    voto = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user','tattooArtist'),)
        index_together = (('user','tattooArtist'),)

class Rating(models.Model):
    tattooArtist = models.ForeignKey(TattooArtist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user','tattooArtist'),)
        index_together = (('user','tattooArtist'),)

class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tattoo = models.ForeignKey(Tattoo, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('user','tattoo'),)
        index_together = (('user','tattoo'),)


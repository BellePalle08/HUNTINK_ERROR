from django.contrib import admin
from .models import TattooArtist, TattooArtistPhoto, TattooArtistStyle, Tattoo, TattooStyle, Review, Rating, Favourites


admin.site.register(TattooArtist)
admin.site.register(TattooArtistPhoto)
admin.site.register(TattooArtistStyle)
admin.site.register(Tattoo)
admin.site.register(TattooStyle)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Favourites)

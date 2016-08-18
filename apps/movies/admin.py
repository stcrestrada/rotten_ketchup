from django.contrib import admin

from apps.movies.models import Movie
from apps.movies.models import Review

from apps.genre.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

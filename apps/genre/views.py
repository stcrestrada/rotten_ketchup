from __future__ import absolute_import

from django.shortcuts import get_object_or_404

from django.db.models import Count

from rest_framework import generics

from apps.movies.models import Movie
from apps.movies.serializers import MovieSerializer

from apps.genre.models import Genre
from apps.genre.serializers import GenreSerializer


class ListCreateGenre(generics.ListCreateAPIView):
    model = Genre
    serializer_class = GenreSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        year = self.request.query_params.get('year', None)
        if year is not None:
            queryset = queryset.filter(movie__year=year)
        else:
            queryset = queryset.filter(movie__id__isnull=False)
        queryset = queryset.values().annotate(movie_count=Count('name')).order_by('-movie_count')
        return queryset


class RetrieveUpdatedDestroyGenre(generics.RetrieveUpdateDestroyAPIView):
    model = Genre
    serializer_class = GenreSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        queryset = queryset.filter(movie__id__isnull=False).values().annotate(movie_count=Count('name')).order_by(
            '-movie_count')
        return queryset


class ListMovieGenre(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        return self.queryset.filter(genres__id=self.kwargs.get('genre_id'))


class RetrieveMovieGenre(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            id=self.kwargs.get('id'),
            genres__id=self.kwargs.get('genre_id'))

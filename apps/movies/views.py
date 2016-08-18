from __future__ import absolute_import

from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from apps.movies.models import Movie
from apps.movies.models import Review

from apps.movies.serializers import MovieSerializer
from apps.movies.serializers import ReviewSerializer


class ListCreateMovie(generics.ListCreateAPIView):
    """
    Performs CRUD operations for Movie queryset
    """
    model = Movie
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = self.model.objects.all()
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__startswith=title)
        return queryset

    @detail_route(['get'])
    def movies(self, request, pk=None):
        self.pagination_class.page_size = 1
        movies = self.model.objects.all()
        page = self.paginate_queryset(movies)

        if page is not None:
            serializer = MovieSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class RetrieveUpdateDestroyMovie(generics.RetrieveUpdateDestroyAPIView):
    """
    Update/Delete Movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ListCreateReview(generics.ListCreateAPIView):
    """
    Performs CRUD operations for Review queryset
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(movie_id=self.kwargs.get('movie_pk'))

    def perform_create(self, serializer):
        movie = get_object_or_404(
            Movie, pk=self.kwargs.get('movie_pk'))
        serializer.save(movie=movie)


class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            movie_id=self.kwargs.get('movie_pk'),
            pk=self.kwargs.get('pk'))

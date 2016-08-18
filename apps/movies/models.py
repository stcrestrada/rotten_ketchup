from __future__ import absolute_import

from django.db import models

from apps.genre.models import Genre

from base.models import BaseModel


class Movie(BaseModel):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Review(BaseModel):
    movie = models.ForeignKey(Movie, related_name='reviews')
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rating = models.SmallIntegerField()

    class Meta:
        unique_together = ['email', 'movie']

    def __str__(self):
        return '{0.rating} by {0.email} for {0.movie}'.format(self)

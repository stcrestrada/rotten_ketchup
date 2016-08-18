from django.db.models import Count

from rest_framework import serializers

from apps.movies.models import Review
from apps.movies.models import Movie


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'review_id',
            'movie',
            'name',
            'email',
            'comment',
            'rating',
            'created_at'
        )

        model = Review

    def validate_rating(self, value):
        if value in range(1, 6):
            return value
        raise serializers.ValidationError("Rating must be integer between 1 and 5.")


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.HyperlinkedRelatedField(
        view_name='genres:genre_detail',
        many=True,
        read_only=True
    )

    class Meta:
        fields = (
            'id',
            'title',
            'year',
            'genres',
        )

        model = Movie

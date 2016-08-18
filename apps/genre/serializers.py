from rest_framework import serializers

from apps.genre.models import Genre


class GenreSerializer(serializers.ModelSerializer):
    movie_count = serializers.IntegerField()
    class Meta:
        fields = ('id', 'name', 'created_at', 'movie_count')

        model = Genre

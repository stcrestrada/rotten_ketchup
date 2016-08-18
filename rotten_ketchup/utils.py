import csv
import os

from django.conf import settings

from apps.movies.models import Movie, Genre

from tqdm import tqdm


def load_data():
    with open(os.path.join(settings.DATA_DIR, 'movies_genres.tsv')) as movie_data:
        reader = csv.reader(movie_data, delimiter='\t')
        for line in tqdm(reader, total=1000):
            title, year, genre = line
            genre, _ = Genre.objects.get_or_create(name=genre)
            movie, _ = Movie.objects.get_or_create(title=title, year=year)
            movie.genres.add(genre)

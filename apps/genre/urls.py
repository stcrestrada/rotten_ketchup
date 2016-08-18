from django.conf.urls import url

from apps.genre.views import ListCreateGenre
from apps.genre.views import RetrieveUpdatedDestroyGenre
from apps.genre.views import ListMovieGenre
from apps.genre.views import RetrieveMovieGenre

urlpatterns = [
    url(r'^$', ListCreateGenre.as_view(), name="genre_list"),
    url(r'^(?P<pk>[^/]+)/$', RetrieveUpdatedDestroyGenre.as_view(), name="genre_detail"),
    url(r'^(?P<genre_id>[^/]+)/movies/$', ListMovieGenre.as_view(), name='movie_genre_list'),
    url(r'^(?P<genre_id>[^/]+)/movies/(?P<id>[^/]+)/$', RetrieveMovieGenre.as_view(),
        name='movie_genre_detail')
]
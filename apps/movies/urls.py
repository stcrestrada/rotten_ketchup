from __future__ import absolute_import

from django.conf.urls import url

from apps.movies.views import ListCreateMovie
from apps.movies.views import RetrieveUpdateDestroyMovie
from apps.movies.views import ListCreateReview
from apps.movies.views import RetrieveUpdateDestroyReview

urlpatterns = [
    url(r'^$', ListCreateMovie.as_view(), name='movie_list'),
    url(r'^(?P<pk>[^/]+)/$', RetrieveUpdateDestroyMovie.as_view(), name='movie_detail'),
    url(r'^(?P<movie_pk>[^/]+)/reviews/$', ListCreateReview.as_view(), name='review_list'),
    url(r'^(?P<movie_pk>[^/]+)/reviews/(?P<pk>[^/]+)/$', RetrieveUpdateDestroyReview.as_view(),
        name='review_detail'),
]

from rest_framework import viewsets

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().select_related("certification")
    serializer_class = MovieSerializer

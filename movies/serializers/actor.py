from ..models import Actor
from rest_framework import serializers
from .movie import MovieDetailSerializer

class ActorListSerializer(serializers.ModelSerializer):

      class Meta:
            model = Actor
            fields = ('id', 'name',)


class ActorSerializer(serializers.ModelSerializer):
      movies = MovieDetailSerializer(many=True, read_only=True)

      class Meta:
            model = Actor
            fields = ('id', 'movies', 'name',)


# class NameSerializer(serializers.ModelSerializer):

#       class Meta:
#             model = Actor
#             fields = ('name',)
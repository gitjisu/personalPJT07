from ..models import Movie, Actor
from rest_framework import serializers
# from .actor import NameSerializer
from .review import ReviewSerializer

class MovieListSerializer(serializers.ModelSerializer):

      class Meta:
            model = Movie
            fields = ('title', 'overview',)


class NameSerializer(serializers.ModelSerializer):

      class Meta:
            model = Actor
            fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
      actors = NameSerializer(many=True, read_only=True)
      review_set = ReviewSerializer(many=True, read_only=True)

      class Meta:
            model = Movie
            fields = '__all__'
            # fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date', 'poster_path',)


class MovieDetailSerializer(serializers.ModelSerializer):

      class Meta:
            model = Movie
            fields = ('title',)
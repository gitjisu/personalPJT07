from ..models import Movie
from rest_framework import serializers
from .review import ReviewSerializer


class MovieListSerializer(serializers.ModelSerializer):

      class Meta:
            model = Movie
            fields = ('title', 'overview',)



class MovieSerializer(serializers.ModelSerializer):
      review_set = ReviewSerializer(many=True, read_only=True)

      class Meta:
            model = Movie
            fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date', 'poster_path',)


class MovieDetailSerializer(serializers.ModelSerializer):

      class Meta:
            model = Movie
            fields = ('title',)
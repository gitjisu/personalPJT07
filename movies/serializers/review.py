from ..models import Movie, Review
from rest_framework import serializers


class ReviewListSerializer(serializers.ModelSerializer):

      class Meta:
            model = Review
            fields = ('title', 'content',)


class MovieTitleSerializer(serializers.ModelSerializer):

      class Meta:
            model = Movie
            fields = ('title',)

class ReviewSerializer(serializers.ModelSerializer):
      movie = MovieTitleSerializer(read_only=True)

      class Meta:
            model = Review
            fields = ('id', 'movie', 'title', 'content',)
            read_only_fields = ('movie',)
            # depth = 1
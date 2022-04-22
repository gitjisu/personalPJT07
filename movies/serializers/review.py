from ..models import Review
from rest_framework import serializers


class ReviewListSerializer(serializers.ModelSerializer):

      class Meta:
            model = Review
            fields = ('title', 'content',)



class ReviewSerializer(serializers.ModelSerializer):
      

      class Meta:
            model = Review
            fields = ('id', 'movie', 'title', 'content')
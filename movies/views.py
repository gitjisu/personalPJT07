
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Actor, Movie, Review
from .serializers.actor import ActorListSerializer, ActorSerializer
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.review import ReviewListSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def actor_list(request):
      actors = get_list_or_404(Actor)
      serializer = ActorListSerializer(actors, many=True)
      return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actors_pk):
      actor = get_object_or_404(Actor, pk=actors_pk)
      serializer = ActorSerializer(actor)
      return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
      movies = get_list_or_404(Movie)
      serializer = MovieListSerializer(movies, many=True)
      return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movies_pk):
      movie = get_object_or_404(Movie, pk=movies_pk)
      serializer = MovieSerializer(movie)
      return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
      reviews = get_list_or_404(Review)
      serializer = ReviewListSerializer(reviews, many=True)
      return Response(serializer.data)
      

@api_view(['POST'])
def review_create(request, movies_pk):
      movie = get_object_or_404(Movie, pk=movies_pk)
      serializer = ReviewSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def review_detail(request, reviews_pk):
      review = get_object_or_404(Review, pk=reviews_pk)

      if request.method == 'GET':
            serializer = ReviewSerializer(review)
            return Response(serializer.data)

      elif request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                  serializer.save()
                  return Response(serializer.data)

      elif request.method == 'DELETE':
            review.delete()
            data = {
                  'delete' : f'review {reviews_pk} is deleted.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
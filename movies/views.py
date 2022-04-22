from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Actor, Movie, Review
from .serializers.actor import ActorListSerializer, ActorSerializer
from .serializers.movie import MovieListSerializer, MovieSerializer, MovieDetailSerializer
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
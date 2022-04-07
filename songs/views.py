from webbrowser import get
from django import shortcuts
from django.shortcuts import render
from .serializers import SongSerializer
from .models import Song
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from songs import serializers


@api_view(['GET', 'POST'])
def get_song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view (['GET', 'PUT', 'DELETE'])
def get_song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response (serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def like_song (request, pk):
    song = get_object_or_404(Song, pk=pk)
    song.likes += 1
    serializer = SongSerializer(song, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

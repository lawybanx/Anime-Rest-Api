# from rest_framework import response
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .serializers import AnimeSerializer
from .models import Anime


@api_view(['GET', 'POST'])
def anime_list(request):
    if request.method == 'GET':
        anime = Anime.objects.all()
        serializer = AnimeSerializer(anime, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

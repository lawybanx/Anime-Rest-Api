from rest_framework import serializers
from .models import Anime


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'name', 'japanese_name', 'description',
                  'score', 'start_date', 'end_date', 'episodes', 'status']

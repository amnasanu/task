from rest_framework import serializers
from .models import Building, Room, RoomType

class RoomSerializer(serializers.ModelSerializer):
    room_number = serializers.IntegerField(source='number')

    class Meta:
        model = Room
        fields = ('room_number', 'price')

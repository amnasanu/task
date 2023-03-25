from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Building, BlockedDay, Room
from .serialilzer import RoomSerializer
from rest_framework import status

class AvailableRoomsView(APIView):
    def get(self, request):
  
        check_in = request.query_params.get('check_in', None)
        check_out = request.query_params.get('check_out', None)
        building_name = request.query_params.get('building', None)

        if not check_in or not check_out or not building_name:
            return Response({'error': 'Missing query parameters'}, status=status.HTTP_400_BAD_REQUEST)

     
        try:
            building = Building.objects.get(name=building_name)
        except Building.DoesNotExist:
            return Response({'error': 'Building not found'}, status=status.HTTP_404_NOT_FOUND)

        blocked_days = BlockedDay.objects.filter(day__range=(check_in, check_out))
        blocked_room_ids = [bd.room_id for bd in blocked_days]
        available_rooms = Room.objects.filter(room_type__building=building).exclude(id__in=blocked_room_ids)

        available_rooms = available_rooms.order_by('price')

       
        serializer = RoomSerializer(available_rooms, many=True)
        return Response(serializer.data)

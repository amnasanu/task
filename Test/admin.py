from django.contrib import admin
from .models import Room, RoomType, Building, BlockedDay
# Register your models here.

admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Building)
admin.site.register(BlockedDay)


from django.urls import path
from .views import AvailableRoomsView

urlpatterns = [
    path('available-rooms/', AvailableRoomsView.as_view(), name='available_rooms'),
]

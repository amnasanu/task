from django.db import models

# Create your models here.


class Building(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    SINGLE = 'Single'
    DOUBLE = 'Double'
    TYPE_CHOICES = [
        (SINGLE, 'Single'),
        (DOUBLE, 'Double'),
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.PositiveSmallIntegerField()
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return str(self.number)

class BlockedDay(models.Model):
    day = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.day)
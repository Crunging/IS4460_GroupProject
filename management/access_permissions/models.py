from django.db import models
from buildings.models import Building
from persons.models import Person
from rooms.models import Room
class Access_Permission(models.Model):
      AccessID = models.AutoField(primary_key=True)
      BuildingID = models.ForeignKey(Building, on_delete=models.CASCADE)
      RoomID = models.ForeignKey(Room, on_delete=models.CASCADE)
      UID = models.ForeignKey(Person, on_delete=models.CASCADE)
      Building_Hours = models.TimeField()
      Room_Hours = models.TimeField()

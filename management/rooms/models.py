from django.db import models
from buildings.models import Building 

class Room(models.Model):  
    RoomID = models.AutoField(primary_key=True) 
    BuildingID = models.ForeignKey(Building, on_delete=models.CASCADE) 
    Room_Number = models.IntegerField()
    Type = models.CharField(max_length=255)


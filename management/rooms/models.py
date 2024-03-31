from django.db import models
class Room(models.model):
    RoomID = models.AutoField
    BuildingID =models.ForeignKey(Building, on_delete=models.Cascade)
    Room_Number =models.IntegerField()
    Type = models.CharField(max_length=255)

# Create your models here.

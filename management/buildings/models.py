from django.db import models
class Building(models.Model):
    BuildingID = models.AutoField
    Building_Name = models.CharField(max_length=150)
    Year_Built = models.DateField(max_length=15)

class Room(models.model):
    RoomID = models.AutoField
    BuildingID =models.ForeignKey(Building, on_delete=models.Cascade)
    Room_Number =models.IntegerField()
    Type = models.CharField(max_length=255)
# Create your models here.



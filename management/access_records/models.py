from django.db import models
from persons.models import Person
from buildings.models import Building
from rooms.models import Room

# Create your models here.
class Access_Records(models.Model):
    RecordID = models.AutoField(primary_key=True)
    UID = models.ForeignKey(Persons, on_delete.CASCADE)
    BuildingID = models.ForeignKey(Building, on_delete=models.CASCADE)
    RoomID = models.ForeignKey(Room, on_delete=models.CASCADE)
    DateTime = models.DateTimeField()

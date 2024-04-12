from django.db import models
from persons.models import Person
from buildings.models import Building
from rooms.models import Room

# Create your models here.
class AccessRecord(models.Model):
    RecordID = models.AutoField(primary_key=True)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

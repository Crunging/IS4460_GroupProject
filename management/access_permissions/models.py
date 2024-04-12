from django.db import models
class Access_Permission(models.Model):
      AccessID = models.AutoField(primary_key=True)
      BuildingID = models.ForeignKey(Buildings, on_delete=models.CASCADE)
      RoomID = models.ForeignKey(Rooms, on_delete=models.CASCADE)
      UID = models.ForeignKey(Persons, on_delete=models.CASCADE)
      Building_Hours = models.TimeField()
      Room_Hours = models.TimeField()

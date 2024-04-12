from django.db import models

class Building(models.Model):
    BuildingID = models.AutoField(primary_key=True)
    Building_Name = models.CharField(max_length=150)
    Year_Built = models.CharField(max_length=150)
    Number_people = models.IntegerField()

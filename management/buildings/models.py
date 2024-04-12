from django.db import models


class Building(models.Model):
    BuildingID = models.AutoField(primary_key=True)
    Building_Name = models.CharField(max_length=150)
    Year_Built = models.DateField(max_length=15)
    Number_people = models.DateField(max_length=15)


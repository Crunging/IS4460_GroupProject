from django.db import models
class Building(models.Model):
    BuildingID = models.AutoField
    Building_Name = models.CharField(max_length=150)
    Year_Built = models.DateField(max_length=15)
# Create your models here.



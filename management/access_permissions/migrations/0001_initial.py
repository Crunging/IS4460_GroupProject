# Generated by Django 5.0.2 on 2024-04-12 02:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buildings', '0003_alter_building_year_built'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access_Permission',
            fields=[
                ('AccessID', models.AutoField(primary_key=True, serialize=False)),
                ('Building_Hours', models.TimeField()),
                ('Room_Hours', models.TimeField()),
                ('BuildingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildings.building')),
            ],
        ),
    ]
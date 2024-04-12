# Generated by Django 5.0.1 on 2024-04-12 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('buildings', '0004_alter_building_number_people'),
        ('persons', '0001_initial'),
        ('rooms', '0002_alter_room_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access_Records',
            fields=[
                ('RecordID', models.AutoField(primary_key=True, serialize=False)),
                ('DateTime', models.DateTimeField()),
                ('BuildingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildings.building')),
                ('RoomID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.room')),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.person')),
            ],
        ),
    ]

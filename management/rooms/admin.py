from django.contrib import admin
from .models import Room, Building

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'building', 'room_number', 'room_type')
    list_filter = ('building',)
    search_fields = ('room_number', 'room_type')
    # Add any other custom configurations as needed

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year_built', 'number_people')
    search_fields = ('name',)
    # Add any other custom configurations as needed



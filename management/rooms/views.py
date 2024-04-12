from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Room  # Correct model import
from django.views import View
from .forms import RoomForm

class RoomList(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'rooms/rooms.view.html', {'rooms': rooms})  # Corrected context dictionary key

class RoomDetail(View):
    def get(self, request, room_id):  # Change 'RoomID' to 'room_id'
        room = Room.objects.get(RoomID=room_id)
        return render(request, 'rooms/rooms_detail.html', {'room': room})
class RoomUpdate(View):
    def get(self, request, RoomID=None):
        if RoomID:
            room = Room.objects.get(pk=RoomID)
        else:
            room = Room()
        form = RoomForm(instance=room)
        return render(request, 'rooms/rooms_update.html', {'room': room, 'form': form})

    def post(self, request, RoomID=None):
        if RoomID:
            room = Room.objects.get(pk=RoomID)
        else:
            room = Room()
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect(reverse("rooms.view"))
        return render(request, 'rooms/rooms_update.html', {'room': room, 'form': form})

class RoomDelete(View):
    def get(self, request, RoomID=None):
        if RoomID:
            room = Room.objects.get(pk=RoomID)
        else:
            room = Room()
        form = RoomForm(instance=room)
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True
        return render(request, 'rooms/rooms_delete.html', {'room': room, 'form': form})

    def post(self, request, RoomID=None):
        room = Room.objects.get(pk=RoomID)
        room.delete()
        return redirect(reverse("rooms.view"))

class RoomCreate(View):
    def get(self, request):
        form = RoomForm()
        return render(request, 'rooms/rooms_add.html', {'form': form})

    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms.view')
        return render(request, 'rooms/rooms_add.html', {'form': form})

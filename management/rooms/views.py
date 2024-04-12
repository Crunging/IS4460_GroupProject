from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Room  # Correct model import
from django.views import View
from .forms import RoomsForm

class RoomsView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'rooms_view.html', {'rooms': rooms})  # Corrected context dictionary key

class RoomsUpdate(View):
    def get(self, request, RoomID=None):
        if RoomID:
            room = Room.objects.get(pk=RoomID)
        else:
            room = Room()
        form = RoomsForm(instance=room)
        return render(request, 'rooms_update.html', {'room': room, 'form': form})

    def post(self, request, RoomID=None):
        if RoomID:
            room = Room.objects.get(pk=RoomID)
        else:
            room = Room()
        form = RoomsForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect(reverse("rooms_update"))
        return render(request, 'rooms_update.html', {'room': room, 'form': form})

class RoomsDelete(View):
    def get(self, request, RoomID=None):
        if RoomID:
            room = Room.objects.get(pk=RoomID)
        else:
            room = Room()
        form = RoomsForm(instance=room)
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True
        return render(request, 'rooms_delete.html', {'room': room, 'form': form})

    def post(self, request, RoomID=None):
        room = Room.objects.get(pk=RoomID)
        room.delete()
        return redirect(reverse("rooms_view"))

class RoomsAdd(View):
    def get(self, request):
        form = RoomsForm()
        return render(request, 'rooms_add.html', {'form': form})

    def post(self, request):
        form = RoomsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms_view')
        return render(request, 'rooms_add.html', {'form': form})

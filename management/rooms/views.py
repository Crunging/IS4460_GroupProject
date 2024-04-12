from django.shortcuts import render, redirect, reverse, get_object_or_404
from buildings.models import rooms
from django.views import View
from .forms import RoomsForm
from rest_framework import generics


class RoomsView(View):

    def get(self,request):

        rooms = Rooms.objects.all()

        return render(request = request,template_name = 'rooms_view.html',context = {'rooms:rooms})

                                                                                    
class RoomsUpdate(View):

    def get(self,request,RoomID=None):

        if RoomID:
            room = Rooms.objects.get(pk=RoomID)
        else:
            room = Room()

        form = RoomForm(instance=room)


       
        return render(request = request,
                      template_name = 'room_update.html',
                      context = {'room':room,'form':form})
    
    def post(self,request,RoomID=None):

        if RoomID:
            room = Room.objects.get(pk=RoomID)
        else:
            room = room()

        form = RoomForm(request.POST,instance=room)

        if form.is_valid():
            room = form.save()

            return redirect(reverse("rooms_update"))
        
        return render(request = request,template_name = 'rooms_update.html',context = {'room':room,'form':form})
     
class RoomDelete(View):

    def get(self,request,RoomID=None):

        if RoomID:
            room = Room.objects.get(pk=RoomID)
        else:
            room = room()

      
        form = RoomForm(instance=room)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'room_delete.html',context = {'room':room,'form':form})
      
    
    def post(self,request,RoomID=None):

        room = Room.objects.get(pk=RoomID)

        room = RoomForm(request.POST,instance=room)

        room.delete()

        return redirect(reverse("room_view"))

class RoomAdd(View):
    def get(self, request):
        form = RoomForm()
        return render(request, 'room_add.html', {'form': form})

    def post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_view')
        return render(request, 'room_add.html', {'form': form})
    

# Create your views here.

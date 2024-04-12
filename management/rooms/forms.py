from django import forms
from rooms.models import Rooms
class RoomsForm(forms.ModelForm):
    class Meta:
        model = movie 
        fields = '__all__'

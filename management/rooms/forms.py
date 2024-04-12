from django import forms
from rooms.models import Rooms
class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms 
        fields = '__all__'

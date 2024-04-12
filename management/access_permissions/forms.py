from django import forms
from .models import Access_Permission

class AccessPermissionForm(forms.ModelForm):
    class Meta:
        model = Access_Permission
        fields = ['BuildingID', 'RoomID', 'UID', 'Building_Hours', 'Room_Hours']

from django import forms
from buildings.models import Building

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'


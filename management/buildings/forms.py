from django import forms
from buildings.models import Building

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


from django import forms
from .models import AccessRecord

class AccessRecordForm(forms.ModelForm):
    class Meta:
        model = AccessRecord
        fields = '__all__'

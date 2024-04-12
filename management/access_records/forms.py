from django import forms
from .models import Access_Records

class AccessRecordForm(forms.ModelForm):
    class Meta:
        model = Access_Records
        fields = '__all__'

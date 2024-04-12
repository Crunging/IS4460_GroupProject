from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Building
from .forms import BuildingForm

class AccessRecordsList(View):
    def get(self, request):
        access_records = AccessRecord.objects.all()
        return render(request=request, template_name='Action_Records/ActionRecords_list.html', context={'Action_Records': Action_Records})
    
class accessrecords(View):
    def get(self, request, RecordID):
        Action_Record = accessrecord.objects.get(RecordID=RecordID)
        return render(request=request, template_name='Action_Records/ActionRecords_detail.html', context={'Action_Record': Action_Record)

class ActionRecordsUpdate(View):
    def get(self, request, RecordID=None):
        if RecordID:
            Action_Record = accessrecord.objects.get(pk=RecordID)
        else:
            Action_Record = Action_Record()
        form = accessrecordForm(instance=Action_Record)
        return render(request=request, template_name='Action_Records/accessrecords_update.html', context={'Action_Records': Action_Records, 'form': form})
    
    def post(self, request, RecordID=None):
        if RecordID:
            Action_Record = Action_Record.objects.get(pk=RecordID)
        else:
            Action_Record = Action_Record()
        form = Acces_Form(request.POST, instance=Action_Record)
        if form.is_valid():
            form.save()
            return redirect(reverse("accessrecord_list"))
        return render(request=request, template_name='Action_Records/accessrecord_update.html', context={'Action_Record': Action_Record, 'form': form})

class accessrecordDelete(View):
    def get(self, request, RecordID=None):
        if RecordID:
            Action_Record = Action_Record.objects.get(pk=RecordID)
        else:
            Action_Record = Action_Record()
        form = accessrecordForm(instance=Action_Record)
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True
        return render(request=request, template_name='Action_Records/accessrecord_delete.html', context={'Action_Record': Action_Record, 'form': form})
      
    def post(self, request, RecordID=None):
        Action_Record = Action_Record.objects.get(pk=RecordID)
        Action_Record.delete()
        return redirect(reverse("accessrecord_list"))

class accessrecordAdd(View):
    def get(self, request):
        form = accessrecordForm()
        return render(request, 'Action_Record/accessrecord_create.html', {'form': form})

    def post(self, request):
        form = accessrecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accessrecord_list'))
        return render(request, 'Action_Records/accessrecord_create.html', {'form': form})














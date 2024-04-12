from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Access_Recordss
from .forms import AccessRecordsForm

class AccessRecordsList(View):
    def get(self, request):
        access_records = AccessRecord.objects.all()
        return render(request=request, template_name='access_records/accesrecords_list.html', context={'access_Records': Access_Recordss})
    
class AccessRecordsDetail(View):
    def get(self, request, RecordID):
        Access_Records = accessrecord.objects.get(RecordID=RecordID)
        return render(request=request, template_name='access_records/accessRecords_detail.html', context={'access_record': Access_Recordss})

class AccessRecordsUpdate(View):
    def get(self, request, RecordID=None):
        if RecordID:
            access_record = AccessRecord.objects.get(pk=RecordID)
        else:
            access_record = Access_Records()
        form = AccessRecordsForm(instance=access_record)
        return render(request=request, template_name='access_records/accessrecords_update.html', context={'access_records': Access_Recordss, 'form': form})
    
    def post(self, request, RecordID=None):
        if RecordID:
            access_record = Access_Records.objects.get(pk=RecordID)
        else:
            access_record = Access_Records()
        form = AccesRecord_Form(request.POST, instance=Access_Records)
        if form.is_valid():
            form.save()
            return redirect(reverse("accessrecord_list"))
        return render(request=request, template_name='access_records/accessrecord_update.html', context={'access_record': Access_Records, 'form': form})

class AccessRecordsDelete(View):
    def get(self, request, RecordID=None):
        if RecordID:
            access_record = Rccess_Record.objects.get(pk=RecordID)
        else:
            access_record = Access_Records()
        form = AccessRecordsForm(instance=Access_Records)
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True
        return render(request=request, template_name='access_records/accessrecord_delete.html', context={'access_record': Access_Records, 'form': form})
      
    def post(self, request, RecordID=None):
        Access_Records = Access_Records.objects.get(pk=RecordID)
        Access_Records.delete()
        return redirect(reverse("accessrecord_list"))

class AccessRecordsAdd(View):
    def get(self, request):
        form = accessrecordForm()
        return render(request, 'Access_Records/accessrecord_create.html', {'form': form})

    def post(self, request):
        form = accessrecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accessrecord_list'))
        return render(request, 'access_records/accessrecord_create.html', {'form': form})














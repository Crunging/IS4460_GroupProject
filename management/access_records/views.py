from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Access_Records
from .forms import AccessRecordForm

class AccessRecordList(View):
    def get(self, request):
        accessrecords = Access_Records.objects.all()
        return render(request, template_name='access_records/accessrecord_list.html', context={'accessrecords': accessrecords})
    
class AccessRecordDetail(View):
    def get(self, request, RecordID):
        accessrecord = Access_Records.objects.get(RecordID=RecordID)
        return render(request=request, template_name='access_records/accessrecord_detail.html', context={'accessrecord': accessrecord})

class AccessRecordUpdate(View):
    def get(self, request, RecordID):
        accessrecord = Access_Records.objects.get(RecordID=RecordID)
        form = AccessRecordForm(instance=accessrecord)
        return render(request=request, template_name='access_records/accessrecord_update.html', context={'form': form})

    def post(self, request, RecordID):
        accessrecord = Access_Records.objects.get(RecordID=RecordID)
        form = AccessRecordForm(request.POST, instance=accessrecord)
        if form.is_valid():
            form.save()
            return redirect(reverse('accessrecord_list'))
        return render(request=request, template_name='access_records/accessrecord_update.html', context={'form': form})


class AccessRecordDelete(View):
    def get(self, request, RecordID):
        accessrecord = Access_Records.objects.get(RecordID=RecordID)
        return render(request=request, template_name='access_records/accessrecord_delete.html', context={'accessrecord': accessrecord})

    def post(self, request, RecordID):
        accessrecord = Access_Records.objects.get(RecordID=RecordID)
        accessrecord.delete()
        return redirect(reverse("accessrecord_list"))

class AccessRecordCreate(View):
    def get(self, request):
        form = AccessRecordForm()
        return render(request, 'access_records/accessrecord_create.html', {'form': form})

    def post(self, request):
        form = AccessRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accessrecord_list'))
        return render(request, 'access_records/accessrecord_create.html', {'form': form})














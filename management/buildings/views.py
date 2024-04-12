from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Building
from .forms import BuildingForm

class BuildingList(View):
    def get(self, request):
        buildings = Building.objects.all()
        return render(request=request, template_name='buildings/building_list.html', context={'buildings': buildings})
    
class BuildingDetail(View):
    def get(self, request, BuildingID):
        building = Building.objects.get(BuildingID=BuildingID)
        return render(request=request, template_name='buildings/building_detail.html', context={'building': building})

class BuildingUpdate(View):
    def get(self, request, BuildingID=None):
        if BuildingID:
            building = Building.objects.get(pk=BuildingID)
        else:
            building = Building()
        form = BuildingForm(instance=building)
        return render(request=request, template_name='buildings/building_update.html', context={'building': building, 'form': form})
    
    def post(self, request, BuildingID=None):
        if BuildingID:
            building = Building.objects.get(pk=BuildingID)
        else:
            building = Building()
        form = BuildingForm(request.POST, instance=building)
        if form.is_valid():
            form.save()
            return redirect(reverse("building_list"))
        return render(request=request, template_name='buildings/building_update.html', context={'building': building, 'form': form})

class BuildingDelete(View):
    def get(self, request, BuildingID=None):
        if BuildingID:
            building = Building.objects.get(pk=BuildingID)
        else:
            building = Building()
        form = BuildingForm(instance=building)
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True
        return render(request=request, template_name='buildings/building_delete.html', context={'building': building, 'form': form})
      
    def post(self, request, BuildingID=None):
        building = Building.objects.get(pk=BuildingID)
        building.delete()
        return redirect(reverse("building_list"))

class BuildingAdd(View):
    def get(self, request):
        form = BuildingForm()
        return render(request, 'buildings/building_create.html', {'form': form})

    def post(self, request):
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('building_list'))
        return render(request, 'buildings/building_create.html', {'form': form})

from django.shortcuts import render, redirect, reverse
from django.views import View
from .models import Building
from .forms import BuildingForm

class BuildingList(View):
    def get(self, request):
        buildings = Building.objects.all()
        return render(request=request, template_name='buildings/building_list.html', context={'buildings': buildings})

class BuildingUpdate(View):
    def get(self, request, buildingID=None):
        if buildingID:
            building = Building.objects.get(pk=buildingID)
        else:
            building = Building()
        form = BuildingForm(instance=building)
        return render(request=request, template_name='buildings/building_update.html', context={'building': building, 'form': form})
    
    def post(self, request, buildingID=None):
        if buildingID:
            building = Building.objects.get(pk=buildingID)
        else:
            building = Building()
        form = BuildingForm(request.POST, instance=building)
        if form.is_valid():
            form.save()
            return redirect(reverse("building_list"))
        return render(request=request, template_name='buildings/building_update.html', context={'building': building, 'form': form})

class BuildingDelete(View):
    def get(self, request, buildingID=None):
        if buildingID:
            building = Building.objects.get(pk=buildingID)
        else:
            building = Building()
        form = BuildingForm(instance=building)
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True
        return render(request=request, template_name='buildings/building_delete.html', context={'building': building, 'form': form})
      
    def post(self, request, buildingID=None):
        building = Building.objects.get(pk=buildingID)
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

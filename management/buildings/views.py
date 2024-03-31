from django.shortcuts import render

class BuildingsView(View):

    def get(self,request):

        buildings = Building.objects.all()

        return render(request = request,template_name = 'buildings_view.html',context = {'buildings:buildings})

class BuildingUpdate(View):

    def get(self,request,buildingID=None):

        if BuildingID:
            building = Building.objects.get(pk=BuildingID)
        else:
            building = Building()

        form = BuildingForm(instance=building)


       
        return render(request = request,
                      template_name = 'building_update.html',
                      context = {'building':building,'form':form})
    
    def post(self,request,BuildingID=None):

        if BuildingID:
            building = Building.objects.get(pk=BuildingID)
        else:
            building = building()

        form = BuildingForm(request.POST,instance=building)

        if form.is_valid():
            building = form.save()

            return redirect(reverse("building_update"))
        
        return render(request = request,template_name = 'building_update.html',context = {'building':building,'form':form})
     
class BuildingDelete(View):

    def get(self,request,BuildingID=None):

        if BuildingID:
            building = Building.objects.get(pk=BuildingID)
        else:
            building = building()

      
        form = BuildingForm(instance=building)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'building_delete.html',context = {'building':building,'form':form})
      
    
    def post(self,request,BuildingID=None):

        building = Building.objects.get(pk=BuildingID)

        building = BuildingForm(request.POST,instance=building)

        building.delete()

        return redirect(reverse("building_view"))

class BuildingAdd(View):
    def get(self, request):
        form = BuildingForm()
        return render(request, 'building_add.html', {'form': form})

    def post(self, request):
        form = BuildingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('building_view')
        return render(request, 'building_add.html', {'form': form})
    


# Create your views here.

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Building
from .forms import BuildingForm

class AccessPermissionsList(View):
    def get(self, request):
        access_permissions = AccessPermission.objects.all()
        return render(request=request, template_name='access_permissions/accesspermissions_list.html', context={'access_permissions': access_permissions})
    
class AccessPermisions(View):
    def get(self, request, AccessID):
        access_permission = AccessPermission.objects.get(AccessID=AccessID)
        return render(request=request, template_name='access_permissions/accesspermissions_detail.html', context={'access_permission': access_permission)

class AccessPermissionsUpdate(View):
    def get(self, request, AccessID=None):
        if AccessID:
            access_permission = AccessPermision.objects.get(pk=AccessID)
        else:
            access_permission = Acces_Permission()
        form = AccessPermissionForm(instance=access_permission)
        return render(request=request, template_name='access_permisions/accesspermisions_update.html', context={'access_permissions': access_permissions, 'form': form})
    
    def post(self, request, AccessID=None):
        if AccessID:
            access_permission = Access_Permision.objects.get(pk=AccessID)
        else:
            access_permission = Acces_Permission()
        form = Acces_Form(request.POST, instance=access_permission)
        if form.is_valid():
            form.save()
            return redirect(reverse("accesspermission_list"))
        return render(request=request, template_name='access_permissions/accesspermission_update.html', context={'access_permission': access_permission, 'form': form})

class AccessPermissionDelete(View):
    def get(self, request, AccessID=None):
        if AccessID:
            access_permission = Acces_Permission.objects.get(pk=AccessID)
        else:
            access_permission = Access_Permission()
        form = AccessPermisionForm(instance=access_permission)
        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True
        return render(request=request, template_name='access_permissions/accesspermission_delete.html', context={'access_permission': access_permission, 'form': form})
      
    def post(self, request, AccessID=None):
        access_permission = Access_Permission.objects.get(pk=AccessID)
        access_permission.delete()
        return redirect(reverse("accesspermission_list"))

class AccessPermissionAdd(View):
    def get(self, request):
        form = AccessPermissionForm()
        return render(request, 'access_permission/accesspermission_create.html', {'form': form})

    def post(self, request):
        form = AccessPermissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accesspermission_list'))
        return render(request, 'access_permissions/accesspermission_create.html', {'form': form})














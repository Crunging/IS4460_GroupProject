from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Access_Permission
from .forms import AccessPermissionForm

class AccessPermissionList(View):
    def get(self, request):
        accesspermissions = Access_Permission.objects.all()
        return render(request, template_name='access_permissions/accesspermission_list.html', context={'accesspermissions': accesspermissions})

class AccessPermissionDetail(View):
    def get(self, request, AccessID):
        accesspermission = Access_Permission.objects.get(AccessID=AccessID)
        return render(request=request, template_name='access_permissions/accesspermission_detail.html', context={'accesspermission': accesspermission})

class AccessPermissionCreate(View):
    def get(self, request):
        form = AccessPermissionForm()
        return render(request, 'access_permissions/accesspermission_create.html', {'form': form})

    def post(self, request):
        form = AccessPermissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accesspermission_list'))
        return render(request=request, template_name='access_permissions/accesspermission_create.html', context={'form': form})

class AccessPermissionUpdate(View):
    def get(self, request, AccessID):
        accesspermission = Access_Permission.objects.get(AccessID=AccessID)
        form = AccessPermissionForm(instance=accesspermission)
        return render(request=request, template_name='access_permissions/accesspermission_update.html', context={'form': form})

    def post(self, request, AccessID):
        accesspermission = Access_Permission.objects.get(AccessID=AccessID)
        form = AccessPermissionForm(request.POST, instance=accesspermission)
        if form.is_valid():
            form.save()
            return redirect(reverse('accesspermission_list'))
        return render(request=request, template_name='access_permissions/accesspermission_update.html', context={'form': form})

class AccessPermissionDelete(View):
    def get(self, request, AccessID):
        accesspermission = Access_Permission.objects.get(AccessID=AccessID)
        return render(request=request, template_name='access_permissions/accesspermission_delete.html', context={'accesspermission': accesspermission})

    def post(self, request, AccessID):
        accesspermission = Access_Permission.objects.get(AccessID=AccessID)
        accesspermission.delete()
        return redirect(reverse('accesspermission_list'))

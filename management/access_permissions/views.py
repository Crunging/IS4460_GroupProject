from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Access_Permission
from .forms import AccessPermissionForm
from persons.models import Person

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


def access_reportroles(request):
    if request.method == 'GET':
        role = request.GET.get('role')
        if role:
            users_with_role = Person.objects.filter(campus_role=role)
            uids_with_role = users_with_role.values_list('uid', flat=True)
            access_permissions = Access_Permission.objects.filter(UID__in=uids_with_role)
        else:
            access_permissions = Access_Permission.objects.all()
        return render(request, 'access_permissions/access_permission_report.html', {'access_permissions': access_permissions})
    return render(request, 'access_permissions/access_permission_report.html', {})
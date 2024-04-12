from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Access_Permission
from .forms import AccessPermissionForm
from django.urls import reverse_lazy

# Create your views here.
# List view for all access records
class AccessPermissionListView(ListView):
    model = Access_Permission
    context_object_name = 'access_permissions'
    template_name = 'access_permissions/accesspermissions_list.html'

# Detail view for a specific access record
class AccessPermissionDetailView(DetailView):
    model = Access_Permission
    context_object_name = 'access_permission'
    template_name = 'access_permission/accesspermission_detail.html'

# Create view for a new access record
class AccessPermissionCreateView(CreateView):
    model = Access_Permission
    form_class = AccessPermissionForm
    template_name = 'access_permission/accesspermission_form.html'

    def get_success_url(self):
        return reverse_lazy('access_permission_detail', kwargs={'pk': self.object.pk})

# Update view for an existing access record
class AccessPermissionUpdateView(UpdateView):
    model = Access_Permission
    form_class = AccessPermissionForm
    template_name = 'access_permissions/accesspermission_form.html'

    def get_success_url(self):
        return reverse_lazy('access_permission_detail', kwargs={'pk': self.object.pk})

# Delete view for an access record
class AccessPermissionDeleteView(DeleteView):
    model = Access_Permission
    context_object_name = 'access_permission'
    template_name = 'access_permissions/accesspermission_confirm_delete.html'
    success_url = reverse_lazy('access_permission_list')

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import AccessRecord
from .forms import AccessRecordForm
from django.urls import reverse_lazy

# Create your views here.
# List view for all access records
class AccessRecordListView(ListView):
    model = AccessRecord
    context_object_name = 'access_records'
    template_name = 'access_records/accessrecord_list.html'

# Detail view for a specific access record
class AccessRecordDetailView(DetailView):
    model = AccessRecord
    context_object_name = 'access_record'
    template_name = 'access_records/accessrecord_detail.html'

# Create view for a new access record
class AccessRecordCreateView(CreateView):
    model = AccessRecord
    form_class = AccessRecordForm
    template_name = 'access_records/accessrecord_form.html'

    def get_success_url(self):
        return reverse_lazy('access_record_detail', kwargs={'pk': self.object.pk})

# Update view for an existing access record
class AccessRecordUpdateView(UpdateView):
    model = AccessRecord
    form_class = AccessRecordForm
    template_name = 'access_records/accessrecord_form.html'

    def get_success_url(self):
        return reverse_lazy('access_record_detail', kwargs={'pk': self.object.pk})

# Delete view for an access record
class AccessRecordDeleteView(DeleteView):
    model = AccessRecord
    context_object_name = 'access_record'
    template_name = 'access_records/accessrecord_confirm_delete.html'
    success_url = reverse_lazy('access_record_list')

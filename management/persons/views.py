from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Person
from .forms import PersonForm
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'persons/home.html'

class PersonList(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(request=request, template_name='persons/person_list.html', context={'persons': persons})

class PersonDetail(View):
    def get(self, request, uid):
        person = Person.objects.get(uid=uid)
        return render(request=request, template_name='persons/person_detail.html', context={'person': person})

class PersonCreate(View):
    def get(self, request):
        form = PersonForm()
        return render(request=request, template_name='persons/person_create.html', context={'form': form})

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('person_list'))
        return render(request=request, template_name='persons/person_create.html', context={'form': form})

class PersonUpdate(View):
    def get(self, request, uid):
        person = Person.objects.get(uid=uid)
        form = PersonForm(instance=person)
        return render(request=request, template_name='persons/person_update.html', context={'form': form})

    def post(self, request, uid):
        person = Person.objects.get(uid=uid)
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect(reverse('person_list'))
        return render(request=request, template_name='persons/person_update.html', context={'form': form})

class PersonDelete(View):
    def get(self, request, uid):
        person = Person.objects.get(uid=uid)
        form = PersonForm(instance=person)
        return render(request=request, template_name='persons/person_delete.html', context={'person': person, 'form': form})

    def post(self, request, uid):
        person = Person.objects.get(uid=uid)
        person.delete()
        return redirect(reverse('person_list'))

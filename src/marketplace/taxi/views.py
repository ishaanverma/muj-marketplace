from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Taxi
from .forms import AddTaxiForm

class TaxiListView(ListView):
    queryset = Taxi.objects.all()
    template_name = "taxi/list.html"

class TaxiDetailView(DetailView):
    queryset = Taxi.objects.all()
    template_name = "taxi/detail.html"

class TaxiCreateView(LoginRequiredMixin, CreateView):
    login_url = "account:login"
    form_class = AddTaxiForm
    model = Taxi
    template_name = "taxi/taxi_create_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(self.request)
        return super().form_valid(form)

class TaxiUpdateView(UpdateView):
    form_class = AddTaxiForm
    model = Taxi
    template_name = "taxi/taxi_update_form.html"

    def get_object(self, *args, **kwargs):
        obj = super(TaxiUpdateView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied() #or Http404
        return obj

class TaxiDeleteView(DeleteView):
    model = Taxi
    success_url = reverse_lazy('taxi:home')

    def get_object(self, *args, **kwargs):
        obj = super(TaxiDeleteView, self).get_object(*args, **kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied() #or Http404
        return obj

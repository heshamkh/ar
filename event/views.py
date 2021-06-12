from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView, ListView
from .models import Event, Asset, Location
from .forms import EventCreationForm, AssetCreationForm, LocationCreationForm
from django.views.generic import ListView, DetailView # new
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin # new
)


class HomePageView(TemplateView):
    template_name = 'events.html'


class AssetListView(ListView):
    model = Asset
    template_name = 'Assets_list.html'


class AssetCreateView(LoginRequiredMixin, CreateView):
    model = Asset
    form_class = AssetCreationForm
    template_name = 'Asset_new.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventListView(ListView):
    model = Event
    template_name = 'events.html'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreationForm
    template_name = 'event_new.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventCreationForm
    template_name = 'event_edit.html'


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event_delete.html'
    success_url = reverse_lazy('events')



class AssetDetailView(DetailView):
    model = Asset
    template_name = 'Asset_detail.html'


class AssetUpdateView(UpdateView):
    model = Asset
    form_class = AssetCreationForm
    template_name = 'Asset_edit.html'


class AssetDeleteView(DeleteView):
    model = Asset
    template_name = 'Asset_delete.html'
    success_url = reverse_lazy('Assets_list')


class LocationListView(ListView):
    model = Location
    template_name = 'location_list.html'


class LocationCreateView( CreateView):
    model = Location
    form_class = LocationCreationForm
    template_name = 'location_new.html'
    # fields = ('Name', 'Photo', 'starting_date', 'ending_date')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LocationDetailView(DetailView):
    model = Location
    template_name = 'location_detail.html'


class LocationUpdateView(UpdateView):
    model = Location
    form_class = LocationCreationForm
    template_name = 'location_edit.html'


class LocationDeleteView(DeleteView):
    model = Location
    template_name = 'location_delete.html'
    success_url = reverse_lazy('location_list')



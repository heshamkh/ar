from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView, ListView
from .models import Event, Asset
from .forms import EventCreationForm
from django.views.generic import ListView, DetailView # new
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin # new
)


class HomePageView(TemplateView):
    template_name = 'home.html'


class AssetListView(ListView):
    model = Asset
    template_name = 'Assets_list.html'


# class AssetCreateView(LoginRequiredMixin, CreateView):
#     model = Asset
#     form_class = EventCreationForm
#     template_name = 'event_new.html'
#     # fields = ('Name', 'Photo', 'starting_date', 'ending_date')
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


class EventListView(ListView):
    model = Event
    template_name = 'events.html'


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventCreationForm
    template_name = 'event_new.html'
    # fields = ('Name', 'Photo', 'starting_date', 'ending_date')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EventDetailView(DetailView): # new
    model = Event
    template_name = 'event_detail.html'


class EventUpdateView(UpdateView): # new
    model = Event
    form_class = EventCreationForm
    template_name = 'event_edit.html'


class EventDeleteView(DeleteView): # new
    model = Event
    template_name = 'event_delete.html'
    success_url = reverse_lazy('events')



from django.views.generic import TemplateView, ListView
from .models import Event


class HomePageView(TemplateView):
    template_name = 'home.html'


class EventListView(ListView):
    model = Event
    template_name = 'events.html'

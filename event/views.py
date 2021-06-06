from django.views.generic import TemplateView, ListView
from .models import Event
from .forms import EventCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin # new
)


class HomePageView(TemplateView):
    template_name = 'home.html'


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

    # def sample_view(request):
    #     current_user = request.user
    #     print
    #     current_user.id



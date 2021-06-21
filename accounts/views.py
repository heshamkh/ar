from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm ,CustomUserChangeForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfilePageView(generic.TemplateView):
    template_name = 'profile.html'


class ProfileEditPageView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'profile_edit.html'

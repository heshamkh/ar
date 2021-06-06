from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Event, Location ,Asset


class EventCreationForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['Name', 'Photo', 'Locations', 'Assets', 'starting_date', 'ending_date']

    name = forms.CharField()
    starting_date = forms.DateField(
        widget=forms.DateInput(
            format=('%d-%m-%Y'),
            attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}))
    ending_date = forms.DateField(
        widget=forms.DateInput(
            format=('%d-%m-%Y'),
            attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}))

    Photo=forms.ImageField()

    Locations = forms.ModelMultipleChoiceField(
        queryset=Location.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    Assets=forms.ModelMultipleChoiceField(
        queryset=Asset.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


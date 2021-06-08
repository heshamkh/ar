from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Event, Location ,Asset


class EventCreationForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['Name', 'Photo', 'Locations', 'Assets', 'starting_date', 'ending_date']
        widgets = {
            'starting_date': forms.DateInput(format=('%Y-%m-%d'),
                                             attrs={'class': 'datepicker1', 'placeholder': 'Select Date', 'type': 'date'}),
            'ending_date': forms.DateInput(format=('%Y-%m-%d'),
                                             attrs={'class': 'datepicker2', 'placeholder': 'Select Date',
                                                    'type': 'date'})
        }

    name = forms.CharField()

    Photo = forms.ImageField()

    Locations = forms.ModelMultipleChoiceField(
        queryset=Location.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    Assets=forms.ModelMultipleChoiceField(
        queryset=Asset.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


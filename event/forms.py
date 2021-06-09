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


class AssetCreationForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ['code', 'featured_image', 'Google_maps_link', 'ASSETS_TYPE', 'Expiry_date', 'Expiry_time']
        widgets = {
            'Expiry_date': forms.DateInput(format=('%Y-%m-%d'),
                                             attrs={'class': 'datepicker1', 'placeholder': 'Select Date', 'type': 'date'}),
            'Expiry_time': forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
        }

    code = forms.CharField()
    Google_maps_link = forms.CharField()

    featured_image = forms.ImageField()

    ASSETS_TYPE = forms.Select()


class LocationCreationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['Name', 'Longitude', 'Latitude', 'Google_maps_link', 'Plus_code', 'Radius', 'Assets']
        widgets = {
            'Expiry_date': forms.DateInput(format=('%Y-%m-%d'),
                                             attrs={'class': 'datepicker1', 'placeholder': 'Select Date', 'type': 'date'}),
            'Expiry_time': forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
        }

    code = forms.CharField()
    Longitude=forms.NumberInput()
    Latitude = forms.NumberInput()
    Radius = forms.NumberInput()
    Google_maps_link = forms.CharField()
    Plus_code = forms.CharField()
    Assets = forms.ModelMultipleChoiceField(
        queryset=Asset.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    locations = forms.ModelMultipleChoiceField(queryset=Location.objects.all())

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['locations'] = [t.pk for t in
                                  kwargs['location'].location_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    # Overriding save allows us to process the value of 'toppings' field
    def save(self, commit=True):
        # Get the unsaved Pizza instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            # This is where we actually link the pizza with toppings
            instance.location_set.clear()
            for location in self.cleaned_data['locations']:
                instance.course_set.add(location)

        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        # Just like this
        # if commit:
        instance.save()
        self.save_m2m()

        return instance

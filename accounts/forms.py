from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper

from intl_tel_input.widgets import IntlTelInputWidget

from django.forms.widgets import TextInput


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('profilePic', 'phone_number',)
        # phone = forms.CharField()
        widgets = {
            'phone_number': forms.TextInput( attrs={'class': 'PhoneInput', 'type': 'tel','value': '+962',}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.include_media = False


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ['username', 'first_name', 'last_name', 'email', 'profilePic', 'phone_number']
        # phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': "form-control", }, initial='IN'))
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'PhoneInput', 'type': 'tel','value': '+962', },),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.include_media = False



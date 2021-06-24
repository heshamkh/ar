from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from intl_tel_input.widgets import IntlTelInputWidget


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('profilePic', 'phone',)
        phone = PhoneNumberField(widget=IntlTelInputWidget(),
                                 required=False,
                                 initial='+52')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ['username', 'first_name', 'last_name', 'email', 'profilePic', 'phone']
        phone = PhoneNumberField(widget=IntlTelInputWidget(),
                                 required=False,
                                 initial='+52')



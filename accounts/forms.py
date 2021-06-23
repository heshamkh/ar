from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('profilePic', 'phone',)
        phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': "form-control", }, initial='IN'))


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ['username', 'first_name', 'last_name', 'email', 'profilePic', 'phone']
        phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': "form-control", }, initial='IN'))



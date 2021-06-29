from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from intl_tel_input.widgets import IntlTelInputWidget


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('profilePic', 'phone',)
        phone = forms.CharField(widget=IntlTelInputWidget(
                visible_input_attrs={
                    'size': '30',
                    'class': 'form-control',
                },
                hidden_input_attrs={
                    'class': 'form-control',

                }
            ))

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ['username', 'first_name', 'last_name', 'email', 'profilePic', 'phone']
        # phone = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': "form-control", }, initial='IN'))
        phone = forms.CharField(widget=IntlTelInputWidget(
                    visible_input_attrs={
                        'size': '30',
                        'class': 'form-control',
                    },
                    hidden_input_attrs={
                        'class': 'form-control',

                    }
                ))



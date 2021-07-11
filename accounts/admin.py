from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'profilePic', 'phone_number', 'is_staff', ]  # new
    fieldsets = UserAdmin.fieldsets + (  # new
        (None, {'fields': ('profilePic', 'phone_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (  # new
        (None, {'fields': ('profilePic', 'phone_number', )}),
    )

#this just  test
admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # forms to add and change user instances
    form = UserAdminChangeForm # update view
    add_form = UserAdminCreationForm # create view

    # fields to be used when diaplying the user model.
    # these override the definitions on the base UserAdmin
    list_display = ('email', 'first_name', 'last_name', 'confirm', 'admin', 'staff', 'active')
    list_filter = ('admin', 'staff', 'confirm', 'active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('admin', 'staff', 'confirm', 'active',)}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides the get_fieldsets to use this attribute when creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

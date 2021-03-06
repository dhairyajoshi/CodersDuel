from django.contrib import admin
from .models import SubmissionCode
from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('username', 'first_name',)
    list_filter = ( 'username', 'first_name', 'is_active', 'is_staff')
    list_display = ('username', 'id', 'first_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'first_name','password')}),  
        ('Permissions', {'fields': ('is_staff', 'is_active','user_permissions')}),
        
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)

admin.site.register(SubmissionCode)
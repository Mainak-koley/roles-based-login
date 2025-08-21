from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User)
class CustomUserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets +('Profile' , {'fields' : ('address' , 'role' , 'contact')})
    fieldsets =  UserAdmin.fieldsets + (
            ('Profile', {'fields':  ('address' , 'role' , 'contact')}), # Add your custom field names
        )
    list_display = UserAdmin.list_display + ('address' , 'role' , 'contact')
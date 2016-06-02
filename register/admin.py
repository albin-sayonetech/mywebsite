from django.contrib import admin

# Register your models here.
from login.models import UserDetails


admin.site.register(UserDetails)
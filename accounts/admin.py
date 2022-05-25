from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Customer


admin.site.register(Employee)
admin.site.register(Customer)



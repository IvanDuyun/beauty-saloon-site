from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField


class Customer(AbstractUser):
    """Профиль клиента"""
    number = PhoneNumberField(unique=False, null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)

    objects = UserManager()
    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.first_name

class Workday(models.Model):
    """Рабочий день"""
    date = models.DateField()

    class Meta:
        db_table = 'workday'

class Employee(models.Model):
    """Профиль сотрудника"""
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    patronymic = models.CharField(max_length=150, null=True, blank=True)
    number = PhoneNumberField(unique=False, null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    schedule = models.ForeignKey(Workday, on_delete=models.CASCADE, null=True, blank=True)

    objects = UserManager()
    class Meta:
        db_table = 'employee'

    def __str__(self):
        return self.user.first_name


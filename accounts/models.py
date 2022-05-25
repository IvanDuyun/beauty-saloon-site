from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField


class Customer(AbstractUser):
    """Профиль клиента"""
    number = PhoneNumberField(unique=False, null=False, blank=False)
    birth_date = models.DateField(null=True, blank=True)

    objects = UserManager()
    class Meta:
        db_table = 'customer'

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

class Visit(models.Model):
    """Прием"""
    date = models.DateTimeField('Дата и время приема')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    done = models.BooleanField()

    class Meta:
        db_table = 'visit'

class Service(models.Model):
    """Услуга"""
    name = models.CharField('Название услуги', max_length=250, blank=True)
    cost_price = models.PositiveIntegerField('Себестоимость')
    price = models.PositiveIntegerField('Стоимость')
    description = models.TextField('Стоимость')
    duration = models.DurationField('Продолжительность')

    class Meta:
        db_table = 'service'

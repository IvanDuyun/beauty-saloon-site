from django.db import models
from django.conf import settings
from accounts.models import Employee
from service.models import Service

class Visit(models.Model):
    """Прием"""
    date = models.DateTimeField('Дата и время приема')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    done = models.BooleanField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        db_table = 'visit'

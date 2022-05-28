from django.db import models

class Service(models.Model):
    """Услуга"""
    name = models.CharField('Название услуги', max_length=250, blank=True)
    cost_price = models.PositiveIntegerField('Себестоимость')
    price = models.PositiveIntegerField('Стоимость')
    description = models.TextField('Описание')
    duration = models.DurationField('Продолжительность')

    class Meta:
        db_table = 'service'

    def __str__(self):
        return self.name

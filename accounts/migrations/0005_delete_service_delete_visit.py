# Generated by Django 4.0.4 on 2022-05-27 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_employee_patronymic_alter_employee_position_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Visit',
        ),
    ]

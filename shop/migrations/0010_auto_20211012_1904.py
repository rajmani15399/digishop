# Generated by Django 3.2.2 on 2021-10-12 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20190330_1746'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderUpdate',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
    ]

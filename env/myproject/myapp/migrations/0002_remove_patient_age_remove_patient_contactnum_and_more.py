# Generated by Django 5.0.3 on 2024-03-27 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='contactnum',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='status',
        ),
    ]

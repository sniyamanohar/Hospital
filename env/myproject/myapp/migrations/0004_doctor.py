# Generated by Django 5.0.3 on 2024-03-28 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_patient_password1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('password1', models.CharField(max_length=150)),
            ],
        ),
    ]
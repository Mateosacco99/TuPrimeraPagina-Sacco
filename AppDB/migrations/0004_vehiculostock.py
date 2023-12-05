# Generated by Django 4.2.7 on 2023-12-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDB', '0003_delete_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehiculoStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo_vehiculo', models.CharField(max_length=30)),
                ('ano_vehiculo', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('disponible', models.BooleanField()),
            ],
        ),
    ]

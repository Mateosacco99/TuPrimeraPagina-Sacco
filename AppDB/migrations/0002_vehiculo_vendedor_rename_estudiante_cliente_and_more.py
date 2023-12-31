# Generated by Django 4.2.7 on 2023-12-04 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo_vehiculo', models.CharField(max_length=30)),
                ('ano_vehiculo', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Cliente',
        ),
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]

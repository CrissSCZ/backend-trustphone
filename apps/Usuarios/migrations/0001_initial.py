# Generated by Django 5.2.1 on 2025-05-23 05:11

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tiendas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
                ('rol', models.CharField(choices=[('admin', 'Admin'), ('encargado', 'Encargado'), ('vendedor', 'Vendedor')], max_length=100)),
                ('activo', models.BooleanField(default=True)),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tiendas.tienda')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuario',
            },
        ),
    ]

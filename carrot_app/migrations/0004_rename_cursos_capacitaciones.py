# Generated by Django 5.0.2 on 2024-03-15 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrot_app', '0003_remove_cursos_fecha_de_finalizacion_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cursos',
            new_name='Capacitaciones',
        ),
    ]

# Generated by Django 4.0.5 on 2022-08-09 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSpa', '0002_alter_usuario_dni_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dni',
            field=models.IntegerField(),
        ),
    ]

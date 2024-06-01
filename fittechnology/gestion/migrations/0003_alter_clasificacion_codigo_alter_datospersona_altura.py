# Generated by Django 5.0.6 on 2024-05-31 16:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestion", "0002_datospersona_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clasificacion",
            name="codigo",
            field=models.CharField(
                max_length=25,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Solo carácteres permitidos", regex="^[A-Z - ]*$"
                    )
                ],
                verbose_name="Código",
            ),
        ),
        migrations.AlterField(
            model_name="datospersona",
            name="altura",
            field=models.IntegerField(verbose_name="Altura en centímetros"),
        ),
    ]

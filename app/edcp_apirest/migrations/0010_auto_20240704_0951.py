# Generated by Django 3.2.25 on 2024-07-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcp_apirest', '0009_auto_20240704_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pays',
            name='label',
            field=models.CharField(max_length=100, verbose_name='Nom du Pays'),
        ),
        migrations.AlterField(
            model_name='secteur',
            name='label',
            field=models.CharField(max_length=100, verbose_name="Secteur d'Activité"),
        ),
        migrations.AlterField(
            model_name='secteur',
            name='ordre',
            field=models.IntegerField(verbose_name="Ordre d'Affichage"),
        ),
        migrations.AlterField(
            model_name='secteur',
            name='sensible',
            field=models.BooleanField(verbose_name='Est Sensible'),
        ),
    ]

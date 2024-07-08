# Generated by Django 3.2.25 on 2024-07-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcp_apirest', '0013_alter_pays_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='secteur',
            options={'verbose_name': 'Secteur', 'verbose_name_plural': 'Secteurs'},
        ),
        migrations.AlterModelOptions(
            name='typeclient',
            options={'verbose_name': 'Type Client', 'verbose_name_plural': 'Type Clients'},
        ),
        migrations.AlterField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='Est lu'),
        ),
    ]

# Generated by Django 3.2.25 on 2024-07-02 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edcp_apirest', '0005_remove_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Secteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('sensible', models.BooleanField()),
                ('ordre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100, null=True)),
                ('sensible', models.BooleanField(null=True)),
                ('ordre', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('raisonsociale', models.CharField(max_length=100)),
                ('representant', models.CharField(max_length=100)),
                ('rccm', models.CharField(max_length=100, null=True)),
                ('secteur_description', models.CharField(max_length=100, null=True)),
                ('presentation', models.CharField(max_length=255, null=True)),
                ('telephone', models.CharField(max_length=20, null=True)),
                ('email_contact', models.CharField(max_length=100, null=True)),
                ('site_web', models.CharField(max_length=100, null=True)),
                ('ville', models.CharField(max_length=100, null=True)),
                ('adresse_geo', models.CharField(max_length=100, null=True)),
                ('adresse_bp', models.CharField(max_length=100, null=True)),
                ('gmaps_link', models.CharField(max_length=255, null=True)),
                ('effectif', models.IntegerField(null=True)),
                ('pays', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edcp_apirest.pays')),
                ('secteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edcp_apirest.secteur')),
                ('typeclient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edcp_apirest.typeclient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

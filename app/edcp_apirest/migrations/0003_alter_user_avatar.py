# Generated by Django 3.2.25 on 2024-05-15 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edcp_apirest', '0002_alter_user_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='avatars/'),
        ),
    ]

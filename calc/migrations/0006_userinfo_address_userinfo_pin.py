# Generated by Django 5.1.5 on 2025-02-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_rename_ownerlogin_ownerinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='pin',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-17 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Профіль користувача', 'verbose_name_plural': 'Профілі користувачів'},
        ),
    ]

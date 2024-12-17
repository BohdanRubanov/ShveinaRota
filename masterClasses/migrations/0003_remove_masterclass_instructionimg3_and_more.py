# Generated by Django 5.1.3 on 2024-12-16 19:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterClasses', '0002_masterclass_instructionimg1_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterclass',
            name='instructionImg3',
        ),
        migrations.AddField(
            model_name='masterclass',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='examplesImg1',
            field=models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото-приклад1'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='examplesImg2',
            field=models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото-приклад2'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='examplesImg3',
            field=models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото-приклад3'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='injuredImg1',
            field=models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото на пораненому 1'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='injuredImg2',
            field=models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото на пораненому 2'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='injuredImg3',
            field=models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото на пораненому 3'),
        ),
        migrations.AddField(
            model_name='masterclass',
            name='video',
            field=models.URLField(blank=True, null=True, verbose_name='Посилання на відео'),
        ),
    ]
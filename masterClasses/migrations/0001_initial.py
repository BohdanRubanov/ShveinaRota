<<<<<<< HEAD
# Generated by Django 4.1.7 on 2024-12-17 20:15

=======
# Generated by Django 5.1.3 on 2024-12-17 21:22

import django.db.models.deletion
>>>>>>> bf638fa2ba0c71065830537bf3a96395f4bbfc5d
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('instructionImg1', models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото-інструкція1')),
                ('instructionImg2', models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото-інструкція2')),
                ('video', models.URLField(blank=True, null=True, verbose_name='Посилання на відео')),
                ('examplesImg1', models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото-приклад1')),
                ('examplesImg2', models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото-приклад2')),
                ('examplesImg3', models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото-приклад3')),
                ('injuredImg1', models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото на пораненому 1')),
                ('injuredImg2', models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото на пораненому 2')),
                ('injuredImg3', models.ImageField(blank=True, null=True, upload_to='masterclass_images/', verbose_name='Фото на пораненому 3')),
                ('information', models.TextField(verbose_name='Інформація')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Час публікації')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Майстер-клас',
                'verbose_name_plural': 'Майстер-класи',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Коментарій')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Час публікації')),
<<<<<<< HEAD
                ('master_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='masterClasses.masterclass')),
            ],
            options={
                'verbose_name': 'Коментарі',
                'verbose_name_plural': 'Коментарі',
            },
=======
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('master_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='masterClasses.masterclass')),
            ],
>>>>>>> bf638fa2ba0c71065830537bf3a96395f4bbfc5d
        ),
    ]

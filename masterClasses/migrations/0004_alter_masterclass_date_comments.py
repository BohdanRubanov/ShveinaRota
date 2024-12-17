# Generated by Django 5.1.3 on 2024-12-17 09:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterClasses', '0003_remove_masterclass_instructionimg3_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterclass',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Час публікації'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Коментарій')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Час публікації')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('master_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='masterClasses.masterclass')),
            ],
        ),
    ]

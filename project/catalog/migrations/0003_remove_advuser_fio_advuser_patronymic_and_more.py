# Generated by Django 5.1.4 on 2024-12-10 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_advuser_fio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advuser',
            name='fio',
        ),
        migrations.AddField(
            model_name='advuser',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='advuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Фамилия'),
        ),
    ]

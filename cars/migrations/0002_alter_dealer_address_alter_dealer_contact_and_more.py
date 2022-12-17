# Generated by Django 4.1.4 on 2022-12-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='address',
            field=models.TextField(default='', verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='contact',
            field=models.IntegerField(verbose_name='Contacts'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='worker_hours',
            field=models.TextField(default='', verbose_name='Worker hours'),
        ),
    ]

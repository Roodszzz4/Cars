# Generated by Django 4.1.3 on 2022-11-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='dealer',
            field=models.ManyToManyField(blank=True, to='car.dealer'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='worker_hours',
            field=models.TextField(blank=True, default=''),
        ),
    ]

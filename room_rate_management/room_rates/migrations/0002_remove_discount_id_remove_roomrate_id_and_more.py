# Generated by Django 5.0.6 on 2024-06-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_rates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='id',
        ),
        migrations.RemoveField(
            model_name='roomrate',
            name='id',
        ),
        migrations.AlterField(
            model_name='discount',
            name='discount_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='roomrate',
            name='room_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1.5 on 2023-05-25 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingbackend', '0005_alter_booking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.TextField(),
        ),
    ]

# Generated by Django 4.1.5 on 2023-06-04 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingbackend', '0007_date_remove_booking_date_remove_booking_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='activity',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='pilot',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='tug',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

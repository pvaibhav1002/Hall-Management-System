# Generated by Django 4.2.1 on 2023-11-01 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managerdashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'user_booking',
            },
        ),
    ]

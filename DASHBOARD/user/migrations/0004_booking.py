# Generated by Django 4.2.1 on 2023-10-31 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210423_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('datewanted', models.DateField()),
                ('datereq', models.DateTimeField()),
                ('club', models.CharField(max_length=100)),
                ('event', models.CharField(max_length=100)),
                ('eventdetails', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]

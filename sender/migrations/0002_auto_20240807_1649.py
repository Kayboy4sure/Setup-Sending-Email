# Generated by Django 3.0.7 on 2024-08-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='52eb5c', max_length=6),
        ),
    ]

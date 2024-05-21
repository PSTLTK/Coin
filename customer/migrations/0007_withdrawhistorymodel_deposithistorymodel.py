# Generated by Django 4.2 on 2024-05-11 09:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_withdrawmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('withdraw', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.withdrawmodel')),
            ],
        ),
        migrations.CreateModel(
            name='DepositHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('deposit', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.depositmodel')),
            ],
        ),
    ]
# Generated by Django 4.2 on 2024-05-09 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_coinmodel_user_coin_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='coin_amount',
        ),
        migrations.DeleteModel(
            name='CoinModel',
        ),
    ]

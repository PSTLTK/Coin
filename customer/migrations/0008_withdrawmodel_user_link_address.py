# Generated by Django 4.2 on 2024-05-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_withdrawhistorymodel_deposithistorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawmodel',
            name='user_link_address',
            field=models.TextField(default=None),
        ),
    ]
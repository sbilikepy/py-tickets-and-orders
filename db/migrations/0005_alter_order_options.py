# Generated by Django 4.0.2 on 2023-09-08 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_order_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
    ]

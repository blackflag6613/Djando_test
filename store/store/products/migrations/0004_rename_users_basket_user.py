# Generated by Django 3.2.13 on 2023-01-27 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_basket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='users',
            new_name='user',
        ),
    ]

# Generated by Django 3.1 on 2021-05-07 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('carts', '0002_auto_20210507_1140'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cart_items',
            new_name='CartItem',
        ),
    ]

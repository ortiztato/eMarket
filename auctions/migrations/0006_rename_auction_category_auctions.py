# Generated by Django 4.0.3 on 2022-04-13 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_category_auction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='auction',
            new_name='auctions',
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-15 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_remove_category_auctions_auction_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='auction',
        ),
        migrations.AddField(
            model_name='auction',
            name='bid',
            field=models.ManyToManyField(blank=True, related_name='rel_bid', to='auctions.bid'),
        ),
    ]

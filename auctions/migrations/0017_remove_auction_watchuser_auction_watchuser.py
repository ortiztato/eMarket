# Generated by Django 4.0.3 on 2022-04-18 17:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auction_watchuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='watchuser',
        ),
        migrations.AddField(
            model_name='auction',
            name='watchuser',
            field=models.ManyToManyField(blank=True, null=True, related_name='rel_watchuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
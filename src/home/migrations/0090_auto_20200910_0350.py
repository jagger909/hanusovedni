# Generated by Django 3.1 on 2020-09-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0089_auto_20200816_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='translationsettings',
            name='season_ticket_button_en',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='translationsettings',
            name='season_ticket_button_sk',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='translationsettings',
            name='season_ticket_url',
            field=models.URLField(blank=True),
        ),
    ]
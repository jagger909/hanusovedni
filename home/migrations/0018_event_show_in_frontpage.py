# Generated by Django 2.2.9 on 2020-02-24 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200224_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='show_in_frontpage',
            field=models.BooleanField(default=False),
        ),
    ]

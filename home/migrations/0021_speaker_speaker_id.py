# Generated by Django 2.2.9 on 2020-02-27 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200224_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='speaker_id',
            field=models.IntegerField(default=None, null=True, unique=True),
        ),
    ]

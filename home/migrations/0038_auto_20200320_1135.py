# Generated by Django 3.0.4 on 2020-03-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20200320_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festivalpage',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 2.2.9 on 2020-02-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_auto_20200207_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='short_overview',
            field=models.CharField(blank=True, help_text='Zobrazuje sa na stránke s programom', max_length=255, verbose_name='krátky popis'),
        ),
    ]

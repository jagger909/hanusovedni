# Generated by Django 3.0.4 on 2020-04-07 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_auto_20200323_2245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='festivalpage',
            old_name='formatted_title',
            new_name='formatted_title_sk',
        ),
        migrations.RenameField(
            model_name='festivalpage',
            old_name='headline',
            new_name='headline_sk',
        ),
        migrations.RenameField(
            model_name='festivalpage',
            old_name='hero_buttons',
            new_name='hero_buttons_sk',
        ),
        migrations.RenameField(
            model_name='festivalpage',
            old_name='hero_text',
            new_name='hero_text_sk',
        ),
        migrations.RenameField(
            model_name='festivalpage',
            old_name='video_text',
            new_name='video_text_sk',
        ),
    ]

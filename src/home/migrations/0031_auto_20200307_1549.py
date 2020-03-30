# Generated by Django 3.0.3 on 2020-03-07 14:49

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_festivalpage_headline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festivalpage',
            name='headline',
            field=wagtail.core.fields.StreamField([('headliner', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.PageChooserBlock(page_type=['home.Speaker'])), ('description', wagtail.core.blocks.RichTextBlock())]))], null=True),
        ),
    ]
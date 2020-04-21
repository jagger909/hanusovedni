# Generated by Django 3.0.4 on 2020-04-21 09:28

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('home', '0063_auto_20200419_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('stream_url', models.URLField()),
                ('title_en', models.CharField(blank=True, help_text='Titulok stránky ktorý budú vidieť ostatní návštevníci', max_length=255, verbose_name='titulok')),
                ('body_sk', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.TextBlock())])),
                ('body_en', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.TextBlock())])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
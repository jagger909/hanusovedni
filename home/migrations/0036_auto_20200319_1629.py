# Generated by Django 3.0.3 on 2020-03-19 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('home', '0035_event_related_festival'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='related_festival',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='festival'),
        ),
    ]

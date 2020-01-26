# Generated by Django 2.1.8 on 2019-05-10 10:02

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20190507_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='headersettings',
            name='place',
            field=models.CharField(default='Malá scéna STU', max_length=50),
        ),
        migrations.AddField(
            model_name='headersettings',
            name='title',
            field=models.CharField(default='Bratislavské Hanusove dni', max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='video_text',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='headersettings',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
    ]
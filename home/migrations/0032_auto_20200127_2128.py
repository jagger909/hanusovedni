# Generated by Django 2.2.9 on 2020-01-27 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_eventillustration_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventIllustration',
            new_name='Illustration',
        ),
        migrations.AddField(
            model_name='event',
            name='illustration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Illustration', verbose_name='ilustrácia'),
        ),
    ]

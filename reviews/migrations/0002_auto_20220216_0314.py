# Generated by Django 2.2.5 on 2022-02-15 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='LoggerConfigurationcheck_in',
            new_name='check_in',
        ),
        migrations.AddField(
            model_name='review',
            name='location',
            field=models.IntegerField(default=0),
        ),
    ]

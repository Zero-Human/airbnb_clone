# Generated by Django 2.2.5 on 2022-02-12 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20220212_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='amenity',
            options={'verbose_name_plural': 'Amenities'},
        ),
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'Facilities'},
        ),
        migrations.AlterModelOptions(
            name='houserule',
            options={'verbose_name': 'House Rule'},
        ),
        migrations.AlterModelOptions(
            name='roomtype',
            options={'verbose_name': 'Room Type'},
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=140)),
                ('file', models.ImageField(upload_to='')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rooms.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

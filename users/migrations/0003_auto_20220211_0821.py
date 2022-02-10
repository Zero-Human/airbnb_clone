# Generated by Django 2.2.5 on 2022-02-10 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220211_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('KRW', 'KRW')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Korean', 'Korean')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=10, null=True),
        ),
    ]

# Generated by Django 2.2.5 on 2022-02-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220216_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_secret',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='user',
            name='email_verity',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('KRW', 'KRW')], default='KRW', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('English', 'English'), ('Korean', 'Korean')], default='Korean', max_length=10, null=True),
        ),
    ]

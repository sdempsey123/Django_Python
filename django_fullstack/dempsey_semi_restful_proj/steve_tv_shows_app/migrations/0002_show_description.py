# Generated by Django 2.2 on 2021-04-22 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steve_tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit_app', '0010_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]

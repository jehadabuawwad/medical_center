# Generated by Django 3.1.4 on 2021-11-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0002_auto_20211117_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='malady',
            name='email',
            field=models.CharField(default=None, max_length=55),
        ),
    ]

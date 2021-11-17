# Generated by Django 3.1.4 on 2021-11-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='malady',
            name='age',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='malady',
            name='avg_glucose_level',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='malady',
            name='bmi',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='malady',
            name='ever_married',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5),
        ),
        migrations.AddField(
            model_name='malady',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6),
        ),
        migrations.AddField(
            model_name='malady',
            name='hypertension',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5),
        ),
        migrations.AddField(
            model_name='malady',
            name='name',
            field=models.CharField(default=None, max_length=55),
        ),
        migrations.AddField(
            model_name='malady',
            name='work',
            field=models.CharField(choices=[('govt_job', 'govt_job'), ('never_worked', 'never_worked'), ('private', 'private'), ('self-employed', 'Self-employed'), ('self-employed', 'children')], default='never_worked', max_length=32),
        ),
    ]
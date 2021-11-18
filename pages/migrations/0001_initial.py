# Generated by Django 3.1.4 on 2021-11-17 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Malady',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=55)),
                ('email', models.CharField(default=None, max_length=55)),
                ('mobile', models.IntegerField(default=None)),
                ('age', models.IntegerField(default=None)),
                ('bmi', models.IntegerField(default=None)),
                ('avg_glucose_level', models.IntegerField(default=None)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('ever_married', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5)),
                ('hypertension', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5)),
                ('work', models.CharField(choices=[('govt_job', 'govt_job'), ('never_worked', 'never_worked'), ('private', 'private'), ('self-employed', 'Self-employed'), ('self-employed', 'children')], default='never_worked', max_length=32)),
            ],
        ),
    ]
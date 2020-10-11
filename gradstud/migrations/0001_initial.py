# Generated by Django 3.0.8 on 2020-10-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcadInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=64)),
                ('ugmajor', models.CharField(max_length=64)),
                ('gpa', models.FloatField()),
                ('greq', models.IntegerField()),
                ('grev', models.IntegerField()),
                ('greawa', models.FloatField()),
                ('lor1', models.EmailField(max_length=254)),
                ('lor2', models.EmailField(max_length=254)),
                ('lor3', models.EmailField(max_length=254)),
                ('wmonths', models.IntegerField()),
                ('wtype', models.CharField(max_length=64)),
                ('rmonths', models.IntegerField()),
                ('pubven', models.CharField(max_length=64)),
            ],
        ),
    ]

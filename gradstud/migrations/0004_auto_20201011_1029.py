# Generated by Django 3.0.8 on 2020-10-11 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradstud', '0003_auto_20201011_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='acadinfo',
            name='uid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='acadinfo',
            name='university',
            field=models.IntegerField(default=1),
        ),
    ]

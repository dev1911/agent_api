# Generated by Django 3.0.8 on 2020-07-28 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200728_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='username',
            field=models.CharField(max_length=10),
        ),
    ]
# Generated by Django 3.0.6 on 2020-05-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200517_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posts',
            field=models.CharField(max_length=250),
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.DateField(help_text='Date', null=True),
        ),
    ]

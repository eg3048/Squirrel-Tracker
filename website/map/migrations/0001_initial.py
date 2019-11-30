# Generated by Django 2.2.7 on 2019-11-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=13, help_text='Latitude', max_digits=16)),
                ('longitude', models.DecimalField(decimal_places=13, help_text='Longitude', max_digits=16)),
                ('unique_squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=15, unique=True)),
                ('shift', models.CharField(choices=[('am', 'AM'), ('pm', 'PM')], help_text='Shift', max_length=2)),
                ('date', models.DateField(help_text='Date')),
                ('age', models.CharField(choices=[('Juvenile', 'Juveline'), ('adult', 'Adult')], help_text='Age', max_length=8)),
                ('primary_fur_color', models.CharField(choices=[('cinnamon', 'Cinnamon'), ('white', 'White'), ('gray', 'Gray'), ('black', 'Black')], help_text='Primary fur color', max_length=8)),
                ('location', models.CharField(choices=[('ground plane', 'Ground Plane'), ('above_ground', 'Above Ground')], help_text='Location', max_length=12)),
                ('specific_location', models.CharField(help_text='Specific location', max_length=30)),
                ('running', models.BooleanField(help_text='Running')),
                ('chasing', models.BooleanField(help_text='Running')),
                ('climbing', models.BooleanField(help_text='Climbing')),
                ('eating', models.BooleanField(help_text='Eating')),
                ('foraging', models.BooleanField(help_text='Foraging')),
                ('other_activities', models.CharField(help_text='Other activities', max_length=30)),
                ('kuks', models.BooleanField(help_text='Kuks')),
                ('quaas', models.BooleanField(help_text='Quaas')),
                ('moans', models.BooleanField(help_text='Moans')),
                ('tail_flags', models.BooleanField(help_text='Tail flags')),
                ('tail_twitches', models.BooleanField(help_text='Tail twitches')),
                ('approaches', models.BooleanField(help_text='Approaches')),
                ('indifferent', models.BooleanField(help_text='Indifferent')),
                ('runs_from', models.BooleanField(help_text='Runs from')),
            ],
        ),
    ]

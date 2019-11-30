from django.db import models

class Squirrel(models.Model):
    
    AM = 'am'
    PM = 'pm'
    SHIFT_CHOICES = [
        (AM, 'AM'),
        (PM, 'PM'),
    ]

    JUVENILE = 'Juvenile'
    ADULT = 'adult'
    AGE_CHOICES = [
        (JUVENILE, 'Juveline'),
        (ADULT, 'Adult'),
    ]

    CINNAMON = 'cinnamon'
    WHITE = 'white'
    GRAY = 'gray'
    BLACK = 'black'
    PRIMARY_FUR_COLOR_CHOICES = [
        (CINNAMON, 'Cinnamon'),
        (WHITE, 'White'),
        (GRAY, 'Gray'),
        (BLACK, 'Black'),
    ]

    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above_ground'
    LOCATION_CHOICES = [
        (GROUND_PLANE, 'Ground Plane'),
        (ABOVE_GROUND, 'Above Ground'),
    ]

    latitude = models.DecimalField(
        max_digits=16,
        decimal_places=13,
        help_text='Latitude',
    )

    longitude = models.DecimalField(
        max_digits=16,
        decimal_places=13,
        help_text='Longitude',
    )

    unique_squirrel_id = models.CharField(
        max_length=15,
        help_text='Unique Squirrel ID',
        unique=True
    )

    shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        help_text='Shift',
    )

    date = models.DateField(
        help_text='Date'
    )

    age = models.CharField(
        max_length=8,
        choices=AGE_CHOICES,
        help_text='Age'
    )

    primary_fur_color = models.CharField(
        max_length=8,
        choices = PRIMARY_FUR_COLOR_CHOICES,
        help_text='Primary fur color',
    )


    location = models.CharField(
        max_length=12,
        choices=LOCATION_CHOICES,
        help_text='Location',
    )

    specific_location = models.CharField(
        max_length=30,
        help_text='Specific location',
    )

    running = models.BooleanField(
        help_text='Running',
    )

    chasing = models.BooleanField(
        help_text='Running',
    )

    climbing = models.BooleanField(
        help_text='Climbing',
    )

    eating = models.BooleanField(
        help_text='Eating',
    )

    foraging = models.BooleanField(
        help_text='Foraging',
    )

    other_activities = models.CharField(
        max_length=30,
        help_text='Other activities',
    )

    kuks = models.BooleanField(
        help_text='Kuks',
    )

    quaas = models.BooleanField(
        help_text='Quaas',
    )

    moans = models.BooleanField(
        help_text='Moans',
    )

    tail_flags = models.BooleanField(
        help_text='Tail flags',
    )

    tail_twitches = models.BooleanField(
        help_text='Tail twitches',
    )

    approaches = models.BooleanField(
        help_text='Approaches',
    )

    indifferent = models.BooleanField(
        help_text='Indifferent',
    )

    runs_from = models.BooleanField(
        help_text='Runs from'
    )

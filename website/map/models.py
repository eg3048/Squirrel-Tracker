from django.db import models

class Squirrel(models.Model):
    
    AM = 'am'
    PM = 'pm'
    SHIFT_CHOICES = [
        (AM, 'AM'),
        (PM, 'PM'),
    ]

    JUVENILE = 'juvenile'
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
    ABOVE_GROUND = 'above ground'
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
    )

    shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
        help_text='Shift',
    )

    date = models.DateField(
        help_text='Date',
        null=True,
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
        null=True,
    )

    chasing = models.BooleanField(
        help_text='Running',
        null=True,
    )

    climbing = models.BooleanField(
        help_text='Climbing',
        null=True,
    )

    eating = models.BooleanField(
        help_text='Eating',
        null=True,
    )

    foraging = models.BooleanField(
        help_text='Foraging',
        null=True,
    )

    other_activities = models.CharField(
        max_length=30,
        help_text='Other activities',
    )

    kuks = models.BooleanField(
        help_text='Kuks',
        null=True,
    )

    quaas = models.BooleanField(
        help_text='Quaas',
        null=True,
    )

    moans = models.BooleanField(
        help_text='Moans',
        null=True,
    )

    tail_flags = models.BooleanField(
        help_text='Tail flags',
        null=True,
    )

    tail_twitches = models.BooleanField(
        help_text='Tail twitches',
        null=True,
    )

    approaches = models.BooleanField(
        help_text='Approaches',
        null=True,
    )

    indifferent = models.BooleanField(
        help_text='Indifferent',
        null=True,
    )

    runs_from = models.BooleanField(
        help_text='Runs from',
        null=True,
    )

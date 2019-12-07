from django import forms
from .models import Squirrel
class SquirrelForm(forms.ModelForm):
    """
    latitude = forms.DecimalField(
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    
    longitude = forms.DecimalField(
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    
    unique_squirrel_id = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control'}
        )
    )
    
    shift = forms.ChoiceField(
        choices=Squirrel.SHIFT_CHOICES,
    )
    
    date = forms.DateField(
        help_text='Date',
    )
    
    age = forms.ChoiceField(
        choices=Squirrel.AGE_CHOICES,
        help_text='Age',
    )
    
    primary_fur_color = forms.ChoiceField(
        choices=Squirrel.PRIMARY_FUR_COLOR_CHOICES,
        help_text='Primary fur color',
    )
    
    location = forms.ChoiceField(
        choices=Squirrel.LOCATION_CHOICES,
        help_text='Location',
    )
    
    specific_location = forms.CharField(
        help_text='Specific location',
    )
    
    running = forms.NullBooleanField(
        help_text='Is it running ?',
    )
    
    chasing = forms.NullBooleanField(
        help_text='Is it chasing ?',
    )
    
    climbing = forms.NullBooleanField(
        help_text='Is it climbing ?',
    )
    
    eating = forms.NullBooleanField(
        help_text='Is it eating ?',
    )
    
    foraging = forms.NullBooleanField(
        help_text='Is it foraging ?',
    )
    
    other_activities = forms.CharField(
        help_text='Other activities',
    )
    
    kuks = forms.NullBooleanField(
        help_text='Does it kuk ?',
    )
    
    quaas = forms.NullBooleanField(
        help_text='Does it quaa ?',
    )
    
    moans = forms.NullBooleanField(
        help_text='Does it moan ?',
    )
    
    tail_flags = forms.NullBooleanField(
        help_text='Is the tail flaging ?',
    )
    
    tail_twitches = forms.NullBooleanField(
        help_text='Is the tail twitching ?',
    )
    
    approaches = forms.NullBooleanField(
        help_text='Is it approaching?',
        )
    
    indifferent = forms.NullBooleanField(
        help_text='Is it indifferent ?',
    )
    
    runs_from = forms.NullBooleanField(
        help_text='Is it running away ?',
    )"""
    



    class Meta:
        model=Squirrel
        fields='__all__'

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Squirrel


def map(request):
    return HttpResponse('There should be a map here')

def sightings(request):
    sightings_list = Squirrel.objects.order_by('-date')
    template = loader.get_template('map/sightings.html')
    context = {
        'sightings_list':sightings_list,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Squirrel


def map(request):
    sightings= Squirrel.objects.order_by('-date')[:100]
    template = loader.get_template('map/mappage.html')
    context= {
            'sightings':sightings,
            }
    return HttpResponse(template.render(context, request))

def sightings(request):
    sightings_list = Squirrel.objects.order_by('-date')
    template = loader.get_template('map/sightings.html')
    context = {
        'sightings_list':sightings_list,
    }
    return HttpResponse(template.render(context, request))



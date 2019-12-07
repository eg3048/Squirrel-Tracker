from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Squirrel
from .forms import SquirrelForm


def map(request):
    return HttpResponse('There should be a map here')

def sightings(request):
    sightings_list = Squirrel.objects.order_by('-date')
    template = loader.get_template('map/sightings.html')
    context = {
        'sightings_list':sightings_list,
    }
    return HttpResponse(template.render(context, request))

def add_squirrel(request):
    if request.method=='POST':
            form=SquirrelForm(request.POST)
            if form.is_valid():
                    form.save()
                    return redirect('/map/sightings')
    else:
        form=SquirrelForm()
    context = {
        'form':form,
    }
    return render(request, 'map/add.html', context)


def edit_squirrel(request, squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=squirrel_id)
    if request.method == 'POST':
        #check data with form
        form =SquirrelForm(request.POST, instance=get)
        if form.is_valid():
            form.save()
            return redirect(f'map/sightings')
    else:
        #build empty form
        form = SquirrelForm(instance=Squirrel)
    context = {
        'form':form,
    }
    return render(request, 'map/edit_squirrel.html', context)


# Create your views here.

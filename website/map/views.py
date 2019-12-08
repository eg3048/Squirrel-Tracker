from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Squirrel
from .forms import SquirrelForm
import datetime
from django.core.exceptions import ObjectDoesNotExist



def stats(request):
    adult_count = Squirrel.objects.filter(age='adult').count()
    juvenile_count = Squirrel.objects.filter(age='juvenile').count()
    cinnamon_count = Squirrel.objects.filter(primary_fur_color='cinnamon').count()
    white_count = Squirrel.objects.filter(primary_fur_color='white').count()
    black_count = Squirrel.objects.filter(primary_fur_color='black').count()
    gray_count = Squirrel.objects.filter(primary_fur_color='gray').count()
    context = {
        'title':'Sighing statistics',
        'adult_count':adult_count,
        'juvenile_count':juvenile_count,
        'cinnamon_count':cinnamon_count,
        'white_count':white_count,
        'black_count':black_count,
        'gray_count':gray_count,
    }
    return render(request, 'map/stats.html', context)


def map(request):
    sightings = Squirrel.objects.order_by('-date')[:100]
    context = {
        'sightings':sightings,
        'title':'Map of the 100 most recent sightings'
    }
    return render(request, 'map/map.html', context)

def home(request):
    context = {
        'title':'Squirrel-Tracker'
    }
    return render(request, 'map/home.html', context)

def sightings(request):
    sightings_list = Squirrel.objects.order_by('-date')
    context = {
        'sightings_list':sightings_list,
        'title':"Recent sightings"
    }
    return render(request, 'map/sightings.html', context)

def add_squirrel(request):
    if request.method == 'POST':
            form = SquirrelForm(request.POST)
            if form.is_valid():
                    f = form.save(commit=False)
                    i = '0'
                    exist=True
                    while exist:
                        squirrel_id = f.shift + '-' + f.date.strftime('%m') + f.date.strftime('%d') + '-' + i
                        try:
                            Squirrel.objects.get(unique_squirrel_id=squirrel_id)
                            i = str(int(i) + 1)
                        except ObjectDoesNotExist:
                            f.unique_squirrel_id = squirrel_id
                            exist=False
                    f.save()
                    return redirect('/map/sightings')
            else:
                print(form.errors)
    else:
        form=SquirrelForm()
    context = {
        'form':form,
        'title':"Add your new sighting"
    }
    return render(request, 'map/form.html', context)


def edit_squirrel(request, squirrel_id):
    squirrel = Squirrel.objects.get(unique_squirrel_id=squirrel_id)
    if request.method == 'POST':
        #check data with form
        form =SquirrelForm(request.POST, instance=squirrel)
        if form.is_valid():
            f = form.save(commit=False)
            i = '0'
            exist=True
            while exist:
                squirrel_id = f.shift + '-' + f.date.strftime('%m') + f.date.strftime('%d') + '-' + i
                try:
                    Squirrel.objects.get(unique_squirrel_id=squirrel_id)
                    i = str(int(i) + 1)
                except ObjectDoesNotExist:
                    f.unique_squirrel_id = squirrel_id
                    exist=False
            f.save()
            return redirect('../../')
    else:
        #build empty form
        form = SquirrelForm(instance=squirrel)
    context = {
        'form':form,
        'title':"Edit your sighting"
    }
    return render(request, 'map/form.html', context)


# Create your views here.

from django.urls import path

from . import views

urlpatterns = [
    path('map/', views.map, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/add/', views.add_squirrel),
    path('sightings/<str:squirrel_id>/edit/', views.edit_squirrel),
]

from django.core.management.base import BaseCommand
from map.models import Squirrel
import datetime
import csv

class Command(BaseCommand):
    help = "export Database"

    def add_arguments(self,parser):
        parser.add_argument('path', type=str, help='It Indicates the path where the csv file is')


    def handle(self, *args, **options):
        path = options ['path']
        f = open(path, 'w+')
        writer = csv.writer(f,)
        fields_name = [f.name for f in Squirrel._meta.get_fields()]
        writer.writerow(fields_name)
        for squirrel in Squirrel.objects.all():
            row = [(getattr(squirrel, field)) for field in fields_name]
            writer.writerow(row)
        f.close()



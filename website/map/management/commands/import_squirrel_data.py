import csv
from django.core.management.base import BaseCommand
from map.models import Squirrel
import datetime

class Command(BaseCommand):
        help = 'Import Squirrel database'

        def add_arguments(self, parser):
            parser.add_argument('path', type=str, help='Indicates the path where the csv file is located')


        def handle(self, *args, **options):
            path = options['path']
            print('importing data')
            with open (path) as f:
                reader = csv.reader (f, delimiter=',', quotechar="\"")
                fields_name = next(reader)
                for i, _ in enumerate(fields_name):
                    fields_name[i] = fields_name[i].lower ()
                    fields_name[i] = fields_name[i].replace (' ', '_')
                for row in reader:
                    squirrel = Squirrel()
                    for i, field in enumerate(row):
                        if fields_name[i] in [f.name for f in Squirrel._meta.get_fields()]+['x','y']:
                            if fields_name[i] == 'x':
                                squirrel.latitude = float(field)
                            elif fields_name[i] == 'y':
                                squirrel.longitude = float(field)
                            elif field == 'false':
                                setattr(squirrel, fields_name[i], False)
                            elif field == 'true':
                                setattr(squirrel, fields_name[i], True)
                            elif fields_name[i] == 'date':
                                setattr(squirrel, fields_name[i], datetime.datetime.strptime(field, '%m%d%Y'))
                            elif squirrel._meta.get_field(fields_name[i]).choices != []:
                                setattr(squirrel, fields_name[i], field.lower())
                            else:
                                setattr(squirrel, fields_name[i], field)
                    squirrel.save()
                print("data succesfully imported")

from csv import reader
from django.core.management.base import BaseCommand
from ex09.models import Planets


class Command(BaseCommand):

    help = "Seed data from CSV files"

    def handle(self, *args, **kwargs):
        file_path = "d05/datasets/planets.csv"
        try:
            print('file_path:', file_path)
            with open(file_path, 'r') as csvfile:
                csv_reader = reader(csvfile, delimiter='\t')
                for line in csv_reader:

                    for value in line:
                        if value == 'NULL':
                            line[line.index(value)] = None

                    new_planet = Planets(
                        name=line[0],
                        climate=line[1] or "",
                        diameter=line[2] or 0,
                        orbital_period=line[3] or 0,
                        population=line[4] or 0,
                        rotation_period=line[5] or 0,
                        surface_water=line[6] or 0,
                        terrain=line[7] or "",
                    )

                    if not Planets.objects.filter(name=new_planet.name).exists():
                        new_planet.save()

        except Exception as e:
            self.stdout.write(self.style.ERROR('Error importing data'))
            self.stdout.write(self.style.ERROR(f'{str(e)}'))

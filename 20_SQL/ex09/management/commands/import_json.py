from django.core.management.base import BaseCommand
from ex09.models import People, Planets
import json


class Command(BaseCommand):

    help = "Seed data from CSV files"

    def handle(self, *args, **kwargs):

        try:

            file_path = "d05/datasets/ex09_initial_data.json"

            tables = {
                'ex09.planets': Planets,
                'ex09.people': People
            }

            with open(file_path, 'r') as jsonfile:

                data = json.load(jsonfile)

                for item in data:

                    if item['model'] not in tables.keys():
                        raise Exception("Unknown object type")

                    if item['model'] == 'ex09.planets':

                        new_planet = Planets(
                            id=item['pk'],
                            name=item['fields']['name'] or 0,
                            climate=item['fields']['climate'] or 0,
                            diameter=item['fields']['diameter'] or 0,
                            orbital_period=item['fields']['orbital_period'] or 0,
                            population=item['fields']['population'] or 0,
                            rotation_period=item['fields']['rotation_period'] or 0,
                            surface_water=item['fields']['surface_water'] or 0,
                            terrain=item['fields']['terrain'] or 0,
                            # created=item['fields']['created'],
                            # updated=item['fields']['updated'],
                        )

                        if not Planets.objects.filter(
                            name=new_planet.name
                        ).exists():
                            new_planet.save()

                    elif item['model'] == 'ex09.people':

                        if Planets.objects.filter(
                            id=item['fields']['homeworld']
                        ).exists():

                            new_people = People(
                                id=item['pk'],
                                name=item['fields']['name'],
                                birth_year=item['fields']['birth_year'] or 0,
                                gender=item['fields']['gender'] or 0,
                                eye_color=item['fields']['eye_color'] or 0,
                                hair_color=item['fields']['hair_color'] or 0,
                                height=item['fields']['height'] or 0,
                                mass=item['fields']['mass'] or 0,
                                homeworld=Planets.objects.get(
                                    id=item['fields']['homeworld']
                                ),
                                # created=item['fields']['created'],
                                # updated=item['fields']['updated'],
                            )

                            if not People.objects.filter(
                                name=new_people.name
                            ).exists():
                                new_people.save()

                        else:

                            new_people = People(
                                id=item['pk'],
                                name=item['fields']['name'],
                                birth_year=item['fields']['birth_year'] or 0,
                                gender=item['fields']['gender'] or 0,
                                eye_color=item['fields']['eye_color'] or 0,
                                hair_color=item['fields']['hair_color'] or 0,
                                height=item['fields']['height'] or 0,
                                mass=item['fields']['mass'] or 0,
                                # homeworld=Planets.objects.get(
                                    # id=item['fields']['homeworld']
                                # ),
                                # created=item['fields']['created'],
                                # updated=item['fields']['updated'],
                            )

                            if not People.objects.filter(
                                name=new_people.name
                            ).exists():
                                new_people.save()

            self.stdout.write(self.style.SUCCESS('Data imported successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR('Error importing data'))
            self.stdout.write(self.style.ERROR(f'{str(e)}'))

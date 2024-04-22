from csv import reader
from django.core.management.base import BaseCommand
from ex09.models import People, Planets


class Command(BaseCommand):

    help = "Seed data from CSV files"

    def handle(self, *args, **kwargs):
        file_path = "d05/datasets/people.csv"
        try:
            print('file_path:', file_path)
            with open(file_path, 'r') as csvfile:
                csv_reader = reader(csvfile, delimiter='\t')
                for line in csv_reader:

                    for i, value in enumerate(line):
                        if value == 'NULL':
                            line[line.index(value)] = None

                    if line[7]:
                        planet = Planets.objects.get(name=line[7])

                    print(line)

                    new_people = People(
                        name=line[0],
                        birth_year=line[1] or "",
                        gender=line[2],
                        eye_color=line[3] or "",
                        hair_color=line[4] or "",
                        height=line[5] or 0,
                        mass=line[6] or 0,
                        homeworld=planet if planet else None,
                    )

                    if not People.objects.filter(name=new_people.name).exists():
                        new_people.save()

        except Exception as e:
            self.stdout.write(self.style.ERROR('Error importing data'))
            self.stdout.write(self.style.ERROR(f'{str(e)}'))

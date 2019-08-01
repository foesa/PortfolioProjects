import os
import csv
from django.core.management.base import BaseCommand
from titanic.models import Person


class Command(BaseCommand):
    help = 'Builds database from CSV file'


    def handle(self, *args, **options):
        path = "/home/foesa/Documents/Refactored_Py_DS_ML_Bootcamp-master/13-Logistic-Regression/titanic_test.csv"
        count = True
        with open(path) as f:
            has_header = csv.Sniffer().has_header(f.read(1024))
            f.seek(0)
            reader = csv.reader(f)
            if has_header:
                next(reader)
            for row in reader:
                print(" ".join(row))
                _, created = Person.objects.get_or_create(
                        name=row[2],
                        passengerId=row[0],
                        passengerClass=row[1],
                        sex=row[3],
                        age=row[4],
                        ticket=row[7],
                        fare=row[8],
                    )


#TODO Missing values in file need to fill these in somwhow to prevent errors in creating Database
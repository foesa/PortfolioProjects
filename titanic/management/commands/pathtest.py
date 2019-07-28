import os
import csv
from django.core.management.base import BaseCommand
from titanic.models import Person


class Command(BaseCommand):
    help = 'Builds database from CSV file'


    def handle(self, *args, **options):
        path = "/home/foesa/Documents/Refactored_Py_DS_ML_Bootcamp-master/13-Logistic-Regression/titanic_test.csv"
        count = 0
        with open(path) as f:
            reader = csv.reader(f)
            for row in reader:
                if count != 0:
                    _, created = Person.objects.get_or_create(
                        name=row[2],
                        passengerId=row[0],
                        passengerClass=row[1],
                        sex=row[3],
                        age=row[4],
                        ticket=row[7],
                        fare=row[8],
                        cabin=row[9],
                    )
                    created.save()

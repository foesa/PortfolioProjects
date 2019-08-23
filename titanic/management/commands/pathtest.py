import os
import csv
import pandas as pd
from django.core.management.base import BaseCommand
from titanic.models import Person


def Agefill(database):
    Age = database[0]
    Pclass = database[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age

def farefill(database):
    Fare = database[0]
    Pclass = database[1]

    if pd.isnull(Fare):
        if Pclass == 1:
            return 60
        elif Pclass == 2:
            return 25
        elif Pclass == 3:
            return 10
    else:
            return Fare

# TODO Maybe put into one function to prevent double iteration through the file.
class Command(BaseCommand):
    help = 'Builds database from CSV file'


    def handle(self, *args, **options):
        path = "/home/foesa/Documents/Refactored_Py_DS_ML_Bootcamp-master/13-Logistic-Regression/titanic_train.csv"
        database = pd.read_csv(path)
        database['Age'] = database[['Age', 'Pclass']].apply(Agefill, axis=1)
        database['Fare'] = database[['Fare','Pclass']].apply(farefill,axis=1)
        for row in database.itertuples(index = True, name = "Pandas"):
                _, created = Person.objects.get_or_create(
                    name=getattr(row, 'Name'),
                    passengerId=getattr(row, 'PassengerId'),
                    passengerClass=getattr(row, 'Pclass'),
                    sex=getattr(row, 'Sex'),
                    age=getattr(row, 'Age'),
                    ticket=getattr(row, 'Ticket'),
                    fare=getattr(row, 'Fare'),
                )


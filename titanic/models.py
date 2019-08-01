from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    passengerId = models.IntegerField()
    passengerClass = models.IntegerField()
    sex = models.CharField(max_length=100)
    age = models.FloatField()
    ticket = models.CharField(max_length=100)
    fare = models.FloatField()

    def __str__(self):
        return self.name
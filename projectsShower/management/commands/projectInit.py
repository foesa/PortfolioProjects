from django.core.management.base import BaseCommand
from projectsShower.models import Projects

class Command(BaseCommand):
    help = "Creates entry in Projects database with variables put in handle function"

    def handle(self, *args, **options):
        _, created = Projects.objects.get_or_create(
            title='Titanic Project',
            description="Webapp displaying info on the Titanic's passengers with a Machine Learning aspect",
            technology="Python, Django,Scikit-learn",
            image='/home/foesa/Pictures/Screenshot from 2019-08-18 18-57-21.png'
        )

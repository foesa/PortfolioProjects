from django.shortcuts import render
from titanic.models import Person
from django.db.models import Q


def personIndex(request):
    persons = Person.objects.all()
    context = {
        "persons": persons,
    }
    return render(request, "personIndex.html", context)

def persondetail(request, pk):
    person = Person.objects.get(pk=pk)
    context = {
        "person": person,
    }
    return render(request, "personDetail.html", context)

class searchResultsView():

    def get_queryset(self):
        query = self.request.GET.get('q')
        personList = Person.objects.filter(
            Q(name__icontains=query)
        )
        return personList

# Create your views here.

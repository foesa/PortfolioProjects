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

def searchResultsView(request):
    query = request.GET['search']
    personList = None
    try:
        personList = Person.objects.filter(
            Q(passengerId__exact=int(query)) | Q(ticket__icontains=query)
        )
    except:
        personList = Person.objects.filter(
            Q(name__icontains=query) | Q(ticket__icontains=query)
        )
    context ={
         'persons': personList
    }
    return render(request,"search_results.html",context)

def graphPage(request):
    return()
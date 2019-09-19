import pickle

from django.shortcuts import render, redirect
from titanic.forms import MLForm
from titanic.models import Person
from django.db.models import Q
import pandas as pd


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
    return render(request,"graphPage.html")

def MLInput(request):
    if request.method == "GET":
        form = MLForm()
        return render(request, "MLInputForm.html", {"form": form})
    elif request.method == "POST":
        form = MLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(MLResult,form)


def MLResult(request, details):
    if(request.method == "GET"):
        data = {'PassengerId':[details.p],'Pclass':[details.passengerClass],'Name':[details.name],'Sex':[details.sex],
                'Age':[details.sex],'SibSp':[1],'Parch':[0],'Ticket':[details.ticket],'Fare':[details.fare],'Embarked':[details.embarked]}
        dataframe = pd.dataframe(data)
        sex = pd.get_dummies(dataframe['Sex'], drop_first=True)
        embarked = pd.get_dummies(dataframe['Embarked'], drop_first=True)
        dataframe.drop(['Sex', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)
        dataframe.drop('PassengerId', axis=1, inplace=True)
        pd.concat([dataframe, sex, embarked], axis=1)
        print(dataframe)
        #  filename = "final_model.sav"
        # loaded_model =pickle.load(open(filename,'rb'))


    return render(request,"MLResults.html")
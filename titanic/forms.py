from django import forms
from titanic.models import Person

class MLForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    passengerId = forms.IntegerField(min_value=1)
    passengerClass = forms.ChoiceField(choices=[(1,1), (2,2), (3,3)])
    sex = forms.ChoiceField(choices=[("male","Male"), ("female","Female")])
    age = forms.IntegerField(max_value=100, min_value=1)
    ticket = forms.CharField(required=False, max_length=100)
    fare = forms.IntegerField(min_value=1)

    class Meta:
        model = Person
        fields = '__all__'
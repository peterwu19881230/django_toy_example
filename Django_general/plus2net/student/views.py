from django.shortcuts import render
from .models import student


# Create your views here.

from django.http import HttpResponse
def hello_world(request):
    return HttpResponse('Hello, World!')
	

def home(request):
    return render(request, 'home.html')
    
def display(request):
    st=student.objects.all() # Collect all records from table 
    #return render(request, 'home.html')
    return render(request, 'display.html',{'st':st})
    

'''    
from django.views.generic import ListView
from .models import Person

class PersonListView(ListView):
    model = Person
    template_name = 'people.html'
''' 
    
    
from django_tables2 import SingleTableView
from .models import Person
from .tables import PersonTable


class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'people.html'
    
    
def person_list(request):
    table = PersonTable(Person.objects.all())

    return render(request, "person_list.html", {
        "table": table
    })
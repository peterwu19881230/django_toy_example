
import django_tables2 as tables
from .models import Person
from .models import Person2

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", )



import django_tables2 as tables

class PersonTable2(tables.Table):
    class Meta:
        model = Person2
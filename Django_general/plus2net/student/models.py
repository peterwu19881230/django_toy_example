from django.db import models

# Create your models here.
class student(models.Model):
    
	st_name =models.CharField(max_length=100)
	st_class=models.CharField(max_length=20)
	st_sex  =models.CharField(max_length=20)
	st_mark =models.IntegerField()
	

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full name")


from django.contrib.auth import get_user_model
from django.db import models

class Person2(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    birth_date = models.DateField()


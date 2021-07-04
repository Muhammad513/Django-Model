from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Person(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)

    def __str__(self):
        return self.first_name



class Category(models.Model):
    name=models.TextField(max_length=20)



class Car(models.Model):
    model=models.TextField(max_length=10)
    company=models.TextField(max_length=10)
    price=models.IntegerField(max_length=10)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

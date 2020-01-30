from django.db import models

# Create your models here.
class Employee(models.Model):
    '''Creating Database using Models'''
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)

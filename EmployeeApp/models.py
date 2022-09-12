from django.db import models

# Create your models here.

class Departments(models.Model):
  name = models.CharField(max_length=128)

class Employees(models.Model):
  name = models.CharField(max_length=128)
  department = models.CharField(max_length=128)
  dateOfJoining = models.PositiveBigIntegerField(null=False)
  image = models.CharField(max_length=500)
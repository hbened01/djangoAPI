from django.db import models
from datetime import datetime

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeId = models.AutoField(auto_created = True, primary_key = True, serialize = False)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField(default=datetime.now)
    PhotoFileName = models.CharField(max_length=500)
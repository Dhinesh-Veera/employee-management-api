from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    department_lead = models.CharField(max_length=20) #models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

GENDER_CHOICES = [('M', 'Male'),('F', 'Female')]


class Employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    role = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



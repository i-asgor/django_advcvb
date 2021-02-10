from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=255)
    principal = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.name

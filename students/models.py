from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.CharField(max_length=20)
    name=models.CharField(max_length=40)
    designation=models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
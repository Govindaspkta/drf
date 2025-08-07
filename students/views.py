from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student

# Create your views here.
def students(request):
    students=Student.objects.all()
    return HttpResponse(students)
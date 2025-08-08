from django.urls import path
from . import views


urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),
    # path('students/<int:pk>/',views.deletStudent)

    
    
    #emplpoyee endpoints
    #class based views
    path('employees/',views.Employees.as_view),
]

    
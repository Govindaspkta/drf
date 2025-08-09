from django.urls import path
from . import views


urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),
    # path('students/<int:pk>/',views.deletStudent)

    
    
    #emplpoyee endpoints
    #class based views
    path('employee/',views.EmployeeView.as_view()),
    path('employees/,<int:pk>',views.EmployeeDetails.as_view()),
]

    
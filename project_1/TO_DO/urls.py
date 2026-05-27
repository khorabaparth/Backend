from django.urls import path
from .views import StudentData

urlpatterns = [
    path('students/', StudentData),
    path('students/<int:id>/' , StudentData)
]
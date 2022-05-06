from django.urls import path
from .views import StudentListAPIView, StudentCreateAPIView,StudentDeleteAPIView, StudentDetailAPIView,\
    ClassroomAPIView

urlpatterns = [
    path('student/list/', StudentListAPIView.as_view(), name='student_list_api'),
    path('student/create/', StudentCreateAPIView.as_view(), name='student_create_api'),
    path('student/detail/<int:pk>/', StudentDetailAPIView.as_view(), name='student_detail_api'),
    path('student/delete/<int:pk>/', StudentDeleteAPIView.as_view(), name='student_delete_api'),
    path('classroom/<int:student_capacity>/', ClassroomAPIView.as_view(), name='class_api'),
    
]
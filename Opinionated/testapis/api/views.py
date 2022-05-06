from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .serializers import StudentSerializer, ClassroomSerializer
from testapis.models import Student, Classroom
from mixer.backend.django import mixer



class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

class StudentCreateAPIView(CreateAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()
    permission_classes = []
    authentiication_classes = [] 

class StudentDetailAPIView(RetrieveAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()

class StudentDeleteAPIView(DestroyAPIView):
    serializer_class = StudentSerializer
    model = Student
    queryset = Student.objects.all()
    permission_classes = []
    authentiication_classes = [] 

class ClassroomAPIView(APIView):
    serializer_class = ClassroomSerializer
    model = Student
    queryset = Classroom.objects.all()

    permission_classes = [permissions.IsAuthenticated]
    authentiication_classes = [authentication.TokenAuthentication] #use basic for uusename and pword auth

    def get(self, *args, **kwargs):
        url_number = self.kwargs.get("student_capacity")
        # mixer.blend(Classroom, student_capacity=3)
        classroom_qs = Classroom.objects.filter(student_capacity__lte = url_number)
        serialized_data = ClassroomSerializer(classroom_qs, many=True)

        if serialized_data.is_valid:
            return Response({
                "class_data": serialized_data.data,
                "param": "hello",
            },
            status= status.HTTP_202_ACCEPTED)
        else:
            return Response(
                {"Error": "Could not serialize data"},
                status= status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
                )
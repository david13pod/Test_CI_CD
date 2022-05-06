from pyexpat import model
from rest_framework.serializers import ModelSerializer

from testapis.models import Student , Classroom

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "firstname",
            "lastname",
            "username",
            "admission_number",
            "is_qualified",
            "average_score",
        )

class ClassroomSerializer(ModelSerializer):
    class Meta:
        model = Classroom
        fields = (
            "name",
            "student_capacity",
            "students",
        )
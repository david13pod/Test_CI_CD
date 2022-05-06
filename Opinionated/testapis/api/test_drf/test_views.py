from django.urls import reverse
import pytest
from testapis.models import Student,Classroom
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from django.test import TestCase

pytestmark = pytest.mark.django_db


class TestStudentAPIViews(TestCase):

    def setUp(self):
        self.client =APIClient()

        # from django.contrib.auth.models import User
        self.list_url = reverse('student_list_api')
        self.create_url = reverse('student_create_api')
        # self.detail_url = reverse('student_detail_api')
        # self.delete_url = reverse('student_delete_api')
        # self.new_user  = User.objects.create_user(username="fantom", password="qwerty")
        # self.client.force_login(self.new_user)


    def test_student_list_works(self):
        # create model
        student = mixer.blend(Student, firstname='bella')

        # call url
        # response = self.client.get('/api/student/list/')
        response = self.client.get(self.list_url)
        # print(response)

        # asser
        # -json
        # -status

        assert response.json != None
        assert response.status_code == 200

    def test_student_create_works(self):
        input_data={
            "firstname": "monk",
            "lastname": "dunk",
            "username": "",
            "admission_number": 3445,
            "is_qualified": True,
            "average_score": 100
        }
        response = self.client.post(self.create_url,input_data )
        print(response,self.create_url)

        assert response.json != None
        assert response.status_code == 201
        assert Student.objects.count() == 1

    def test_student_detail_works(self):
        student1 = mixer.blend(Student, firstname='bella')
        student2 = mixer.blend(Student, firstname='kay')
        detail_url1 = reverse('student_detail_api', kwargs={"pk": student1.id})
        # detail_url2 = reverse('student_detail_api',  kwargs={"pk": student1.id})
        
        response = self.client.get(detail_url1)
        print('data',response.data)

        assert response.json != None
        assert response.status_code == 200
        assert response.json()['firstname'] == "bella"
        assert response.json()['username'] == "bella"

    def test_student_delete_works(self):
        student1 = mixer.blend(Student, firstname='bella')
        assert Student.objects.count() == 1
        delete_url1 = reverse('student_delete_api', kwargs={"pk": student1.id})
        
        response = self.client.delete(delete_url1)
        print('data',response.data)

        # assert response.json == None
        assert Student.objects.count() == 0
        assert response.status_code == 204



class TestClassromAPIViews(TestCase):

    def setUp(self):
        self.client =APIClient()

        from django.contrib.auth.models import User
        from rest_framework.authtoken.models import Token
        # method1
        self.new_user  = User.objects.create_user(username="fantom", password="qwerty")
        # self.token = Token.objects.create(user=self.new_user)
        # # print(self.token.key)

        # self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)

        # metthod 2
        self.token_url=reverse("api_token")
        user_data={"username":"fantom", "password":"qwerty"}
        response= self.client.post(self.token_url, user_data)
        # print(response.json())
        self.client.credentials(HTTP_AUTHORIZATION="Token "+response.json()["token"])
        

    def test_classapi_works(self):
        # testing tokens and authorization and auhentication
        class1=mixer.blend(Classroom, student_capacity=30)
        class_url = reverse('class_api', kwargs={"student_capacity": 40})

        response = self.client.get(class_url)
        # print(response.data["class_data"])
        # print(response.json())

        assert response.status_code == 202
        assert response.data["class_data"] != None
        assert response.json()["class_data"][0]["student_capacity"] == class1.student_capacity

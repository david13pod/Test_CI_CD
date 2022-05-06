# from django.test import TestCase
from .models import Student, Classroom
import pytest
from mixer.backend.django import mixer
from hypothesis import strategies as st, given
from hypothesis.extra.django import TestCase

pytestmark = pytest.mark.django_db
# Create your tests here.
class TestStudent(TestCase):
# class TestStudent():

    def setUp(self):
        self.firstname = 'jonq'
        self.lastname = 'doe'
        self.admission_number = 300100
        self.average_score = 75

        # self.student11 = Student.objects.create(
        # firstname=self.firstname,
        # lastname=self.lastname,
        # admission_number=self.admission_number,
        # average_score=self.average_score
        # )
        # self.student11.save()

        # mixer here
        self.student1 = mixer.blend(Student, average_score=100)
        self.student1.save()
        
    # hypothesis
    @given(st.floats(min_value=0, max_value=39.9))
    def test_getgradesfail(self, failscore):
        student2 = mixer.blend(Student, average_score=failscore)
        student2.save()
        assert student2.get_grades() == 'fail'
    
    @given(st.floats(min_value=40, max_value=69.9))
    def test_getgradespass(self, passscore):
        student2 = mixer.blend(Student, average_score=passscore)
        student2.save()
        assert student2.get_grades() == 'pass'
    
    @given(st.floats(min_value=70, max_value=100))
    def test_getgradesexcel(self, excelscore):
        student2 = mixer.blend(Student, average_score=excelscore)
        student2.save()
        assert student2.get_grades() == 'excellent'

    def test_status(self):
        # mixer here
        student2 = Student.objects.create(
        firstname='mary',
        lastname='kay',
        admission_number=200300,
        average_score=39
        )
        student2.save()
        # student2 = mixer.blend(Student)
        # self.assertEqual(self.student1.get_status,'qualified')
        # use pytest assert
        assert student2.get_status== 'not qualified'
    
    def test_admission_unique(self):
        with self.assertRaises(Exception) as raised:
            student2 = Student.objects.create(
            firstname='mary',
            lastname='kay',
            admission_number=300200,
            average_score=39
            )
            student22 = Student.objects.create(
            firstname='cece',
            lastname='willy',
            admission_number=300200,
            average_score=99
            )
            print(1,raised.exception)
        assert'UNIQUE constraint failed' in str(raised.exception)


    def test_mixer(self):
        # mixer here
        student2 = mixer.blend(Student, firstname='jona')
        student2.save()
        print(student2.average_score) # blank field should be filled
        assert student2.firstname =='jona'
    
    # check when people add characters in field
    # put a validator in the firstname to ensure at least on string character is included
    # @given(st.characters())
    # def test_slugify(self, name):
    #     # print('name',name)
    #     student4 = mixer.blend(Student, firstname = name)
    #     student4.save()
    #     result = Student.objects.last()
    #     print(result.username)
    #     assert len(str(result.username)) == len(name)


class TestClassroom(TestCase):
    def test_string(self):
        class1 = mixer.blend(Classroom, name='CIT')
        result = Classroom.objects.last()
        assert str(result) == 'CIT'


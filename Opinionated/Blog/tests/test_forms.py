
from django.test import TestCase, SimpleTestCase
from Blog.forms import PostForm, CommentForm
from django.contrib.auth.models import  User

class TestForms(TestCase):

    def setUp(self):
        self.newuser = User.objects.create_user('John doe', 'view@test.com', 'pass')
        

    def test_valid_postform(self):
        form = PostForm(
            data={
                'author': self.newuser,
                'title':'another blog',
                'text':'Hello blog2'
            }
        )
        # print(len(form.errors))
        self.assertTrue(form.is_valid())
    
    def test_invalid_postform(self):
        form = PostForm(
            data={
            }
        )
        self.assertFalse(form.is_valid())


    def test_valid_commentform(self):
        form = CommentForm(
            data={
                'author':'geust',
                'text':'Hello blog2'
            }
        )

        self.assertTrue(form.is_valid())
from django.test import TestCase, Client
from django.urls import reverse, resolve
from Blog.models import Post,Comment
from django.contrib.auth.models import  User


class TestModels(TestCase):

    def setUp(self):
        self.newuser = User.objects.create_user('John doe', 'view@test.com', 'pass')
        self.post1 = Post.objects.create(
            author= self.newuser,
            title='New blog',
            text='Hello blog'
        )
        self.post1_id = Post.objects.first().id
        self.comment1 = Comment.objects.create(
            post = self.post1,
            author= 'guest',
            text='nice piece'
        )

    def test_approvecomment(self):
        self.comment1.approve()

        self.assertEqual(self.comment1.approved_comment,True)

    def test_publish(self):
        # print(self.post1.published_date)
        self.post1.publish()

        self.assertIsNotNone(self.post1.published_date)
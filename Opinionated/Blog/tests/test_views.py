
import json
from urllib.parse import urlencode
from django.test import TestCase, Client, SimpleTestCase,RequestFactory
from django.urls import reverse, resolve
from Blog.models import Post,Comment
from django.utils import timezone
import datetime
from django.contrib.auth.models import  User
from Blog.views import AboutView, PostCreateView, PostDeleteView,PostDetailView,PostListView,PostUpdateView,DraftListView,\
    add_comment_to_post,comment_approve,comment_remove,post_publish


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('post_list')
        self.newuser = User.objects.create_user('John doe', 'view@test.com', 'pass')
        self.newuser2 = User.objects.create_user('Sbow white', 'view2@test.com', 'pass')
        self.post1 = Post.objects.create(
            author= self.newuser,
            # published_date=timezone.now(),
            title='New blog',
            text='Hello blog'
        )
        self.post1_id = Post.objects.first().id
        self.detail_url = reverse('post_detail', args=[self.post1_id])
        self.new_url =reverse('post_new')
        self.delete_url = reverse('post_remove', args=[self.post1_id])
        self.newcomment_url = reverse('add_comment_to_post', args=[self.post1_id])
        # self.client.login(username="Sbow white", password="pass")
        self.client.force_login(self.newuser)

    def test_list_view_resolves(self):
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Blog/post_list.html')

    def test_create_view_resolves(self):
        data ={
            'title':'another blog',
            'text':'Hello blog2'
        }
        
        # response = self.client.post('/post/new/',data, content_type="application/x-www-form-urlencoded", follow=True)
        response =  self.client.post('/post/new/',data)
        # response = self.client.post('/post/new/',json.dumps(data), content_type='application/json')
        # print(response)
        # import pdb; pdb.set_trace()

        # self.factory = RequestFactory()
        # request = self.factory.post('/post/new/')
        # request.user = self.newuser2

        # my_view = PostCreateView
        # response2 = my_view.as_view()(request,data)
        # print(response2)
        # print(Post.objects.all())


        self.assertEqual(response.status_code, 302) #redirect code
        # self.assertEquals(response.status_code, 200) #redirect code
        self.assertEqual(Post.objects.last().title, 'another blog') 
        self.assertEqual(Post.objects.first().title, 'New blog') 
        # print(Post.objects.all())

    def test_detail_view_resolves(self):
        response = self.client.get(self.detail_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Blog/post_detail.html')
        
    
    def test_addcomment_view_resolves(self):
        data ={
            'author':'guest',
            'text':'nice piece'
        }
        response =  self.client.post(self.newcomment_url,data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.detail_url)
        self.assertEqual(Comment.objects.last().author, 'guest') 

    def test_delete_view_resolves(self):
        response = self.client.delete(self.delete_url)
        # print(Post.objects.all())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)
    


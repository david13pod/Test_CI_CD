from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Blog.views import AboutView, PostCreateView, PostDeleteView,PostDetailView,PostListView,PostUpdateView,DraftListView,\
    add_comment_to_post,comment_approve,comment_remove,post_publish

class TestUrls(SimpleTestCase):

    def test_post_list_resolves(self):
        url = reverse('post_list')
        # print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, PostListView)

    def test_post_create_resolves(self):
        url = reverse('post_new')
        self.assertEqual(resolve(url).func.view_class, PostCreateView)

    def test_post_detail_resolves(self):
        url = reverse('post_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_post_delete_resolves(self):
        url = reverse('post_remove', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDeleteView)

    def test_post_update_resolves(self):
        url = reverse('post_edit', args=[1])
        self.assertEqual(resolve(url).func.view_class, PostUpdateView)

    def test_add_comment_resolves(self):
        url = reverse('add_comment_to_post', args=[1])
        self.assertEqual(resolve(url).func, add_comment_to_post)

    def test_Comment_approve_resolves(self):
        url = reverse('comment_approve', args=[1])
        self.assertEqual(resolve(url).func, comment_approve)


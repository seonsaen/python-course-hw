from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post, Comment


class APIEndpointsTests(APITestCase):
    def setUp(self):
        Post.objects.all().delete()
        Comment.objects.all().delete()
        User.objects.all().delete()

        self.author = User.objects.create_user(username='author', password='123')
        self.reader = User.objects.create_user(username='reader', password='123')

        self.post = Post.objects.create(title='Test Post', text='Hello', author=self.author)
        self.comment = Comment.objects.create(post=self.post, text='Nice post!', author=self.reader)

        self.posts_url = '/api/posts/'
        self.comments_url = '/api/comments/'

    def test_post_list_and_retrieve(self):
        response_list = self.client.get(self.posts_url)
        self.assertEqual(response_list.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_list.data), 1)

        response_detail = self.client.get(f'{self.posts_url}{self.post.id}/')
        self.assertEqual(response_detail.status_code, status.HTTP_200_OK)

    def test_post_create_authorized(self):
        self.client.force_authenticate(user=self.author)
        data = {'title': 'New', 'text': 'Content'}
        response = self.client.post(self.posts_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_create_unauthorized(self):
        data = {'title': 'New', 'text': 'Content'}
        response = self.client.post(self.posts_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_update_by_author(self):
        self.client.force_authenticate(user=self.author)
        response = self.client.patch(f'{self.posts_url}{self.post.id}/', {'title': 'Updated'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_delete_by_reader(self):
        self.client.force_authenticate(user=self.reader)
        response = self.client.delete(f'{self.posts_url}{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_popular_action(self):
        response = self.client.get(f'{self.posts_url}popular/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_list(self):
        response = self.client.get(self.comments_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_comment_create(self):
        self.client.force_authenticate(user=self.reader)
        data = {'post': self.post.id, 'text': 'Another comment'}
        response = self.client.post(self.comments_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_delete_by_author(self):
        self.client.force_authenticate(user=self.reader)
        response = self.client.delete(f'{self.comments_url}{self.comment.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
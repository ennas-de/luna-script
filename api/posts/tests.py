from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse

from .models import Post

# Create your tests here.

class BlogPostTestCase(TestCase):

    def setUp(self, *args, **kwargs):
        self.client = Client()

    def test_get_post_list_view(self, *args, **kwargs):
        response = self.client.get(reverse('list_view'), {}, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_tags_list_view(self, *args, **kwargs):
        response = self.client.get(reverse('tags_list'), {}, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
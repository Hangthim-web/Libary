from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from books.models import Book

from rest_framework.test import APITestCase
# Create your tests here.

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "To kill a mocking bird",
            subtitle= "tkamb",
            author = "Harper Lee",
            isbn="1234567891012"
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(),1)
        self.assertContains(response,self.book)

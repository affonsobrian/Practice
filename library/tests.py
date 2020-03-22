from rest_framework.test import APITestCase

from library.models import Author


class AuthorTestCase(APITestCase):
    def post(self):
        response = self.client.post('/author/', {'name': 'Albert Einstein'}, format='json')
        self.assertEqual(response.status_code, 201)


class BooksTestCase(APITestCase):
    def post(self):
        Author.objects.create(name="Albert Einstein")
        response = self.client.post('/books/', {'name': 'Physics III', 'edition': 1, 'publication_year': 1850,
                                                'authors': [1]}, format='json')
        self.assertEqual(response.status_code, 201)

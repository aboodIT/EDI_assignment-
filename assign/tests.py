from django.urls import reverse, include, path
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from .models import team_model


class TeamModelTests(APITestCase):
    def test_instance(self):
        data = {'name': 'Development'}
        response = self.client.post('/teams/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(team_model.objects.count(), 1)
        self.assertEqual(team_model.objects.get().name, 'Development')

# class AccountTests(APITestCase, URLPatternsTestCase):
#     urlpatterns = [

#         path('', include('assign.urls')),
#     ]

#     def test_create_account(self):
#         """
#         Ensure we can create a new account object.
#         """
#         url = reverse('team_view')
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), {
#         "id": 3,
#         "name": "Development"
#     })


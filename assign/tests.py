from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import team_model


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        #url = reverse('Team_view')
        data = {'name': 'Development'}
        response = self.client.post('/team/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(team_model.objects.count(), 1)
        self.assertEqual(team_model.objects.get().name, 'Development')

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserLoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_user_login(self):
        response = self.client.get(reverse('user_login'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('user_login'), data={
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username='testuser')
        self.assertTrue(user.is_authenticated)

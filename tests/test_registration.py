from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserRegistrationTests(TestCase):
    def test_user_registration(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('register'), data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'fake_first_name',
            'last_name': 'fake_last_name'
        })
        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username='testuser')
        self.assertTrue(user.check_password('testpass123'))

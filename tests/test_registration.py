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

    def test_user_registration_with_invalid_data(self):
        response = self.client.post(reverse('register'), data={
            'username': '',
            'email': 'invalid_email',
            'password1': 'short',
            'password2': 'mismatch'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required.")
        self.assertContains(response, "Enter a valid email address.")
        self.assertContains(response, "Ensure this value has at least 8 characters (it has 5).")
        self.assertContains(response, "The two password fields didn't match.")

    def test_user_registration_with_existing_username(self):
        User.objects.create_user(username='existinguser', password='testpass123')
        response = self.client.post(reverse('register'), data={
            'username': 'existinguser',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A user with that username already exists.")

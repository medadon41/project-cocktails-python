from django.contrib.auth.models import User
from django.test import TestCase

from apps.cauth.models import Profile


class RegistrationTestCase(TestCase):
    def test_registration_post_valid_form(self):
        form_data = {'username': "test123", "password1": "5UwZWCh9JYp8", 'password2': "5UwZWCh9JYp8"}
        response = self.client.post("/register/", data=form_data)
        self.assertEqual(response.status_code, 302)

    def test_registration_profile_creation(self):
        form_data = {'username': "test123", "password1": "5UwZWCh9JYp8", 'password2': "5UwZWCh9JYp8"}
        self.client.post("/register/", data=form_data)

        self.assertTrue(Profile.objects.filter(user__username='test123').exists())


class ProfileViewTestCase(TestCase):
    def setUp(self) -> None:
        form_data = {'username': "test123", "password1": "5UwZWCh9JYp8", 'password2': "5UwZWCh9JYp8"}
        self.client.post("/register/", data=form_data)

    def test_profile_get(self):
        response = self.client.get("/profile/test123")
        print(response)
        self.assertEqual(response.status_code, 200)


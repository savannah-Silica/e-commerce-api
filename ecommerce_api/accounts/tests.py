from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class SignupPageTest(TestCase):
    def test_url_exist_at_correct_locaion_signupview(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
    
    def test_signup_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signup.html')

    def test_signup_form(self):
        response = self.client.post(reverse("signup"), {
            'name': 'testuser',
            'email': 'test@mail.com',
            'address': 'test address',
            'phone_number': '1234567890',
            'password1': 'testpass123',
            'password2': 'testpass123', 
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].name, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'test@mail.com')

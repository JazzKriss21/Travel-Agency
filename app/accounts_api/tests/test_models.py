from django.test import TestCase
from django.contrib.auth import get_user_model

# from accounts_api import models


def sample_user(email='test@test.com', password='testtesttest'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        name = 'testuser'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@TEST.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'testuser',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from accounts_api.serializers import UserProfileSerializer
from accounts_api.models import UserProfile

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from accounts_api import views

class UserProfileViewSet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@foo.com', name='usertest', password='top_secret')
        self.id = self.user.id
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def test_token_auth(self):
        request = self.factory.get('/account/api/profile_api')
        force_authenticate(request, token=self.token.key)
        view = views.UserProfileViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_edit_user(self):
        request = self.factory.patch(f'/account/api/profile_api/', {'email':'edited@edited.com'})
        force_authenticate(request, token=self.token.key)
        view = views.UserProfileViewSet.as_view({'patch': 'partial_update'})
        response = view(request,pk=self.id)
        self.assertEqual(response.status_code, 200)

    def test_edit_user_without_auth(self):
        request = self.factory.patch(f'/account/api/profile_api/', {'email':'edited@edited.com'})
        # force_authenticate(request, token=self.token.key)
        view = views.UserProfileViewSet.as_view({'patch': 'partial_update'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 200)

    def test_delete_user_without_auth(self):
        request = self.factory.delete(f'/account/api/profile_api/')
        # force_authenticate(request, token=self.token.key)
        view = views.UserProfileViewSet.as_view({'delete': 'destroy'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 204)

    def test_delete_user(self):
        request = self.factory.delete(f'/account/api/profile_api/', {'email':'edited@edited.com'})
        force_authenticate(request, token=self.token.key)
        view = views.UserProfileViewSet.as_view({'delete': 'destroy'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 204)



from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from travelpartner.api.serializers import TravelPartnerSerializer
from travelpartner.models import TravelPartner
from travelpartner.api import views

from django.contrib.auth import get_user_model

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

class TravelPartnerTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@foo.com', name='usertest', password='top_secret')
        self.id = self.user.id
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def test_get_travelpartner(self):
        request = self.factory.get('/travelpartner/api/travelpartner')
        force_authenticate(request, token=self.token.key)
        view = views.TravelPartnerViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post_travel_partner(self):
        data = {
        "user": '1',
        "name": "testuser",
        "start_date": '2020-12-22',
        "end_date": '2020-12-24',
        "destination": "testuser",
        "description": "testuser",
        "phone": "123"
        }
        request = self.factory.post(f'/travelpartner/api/travelpartner/', data)
        force_authenticate(request, token=self.token.key)
        view = views.TravelPartnerViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_edit(self):
        request = self.factory.patch(f'/travelpartner/api/travelpartner/', {'name':'edited'})
        force_authenticate(request, token=self.token.key)
        view = views.TravelPartnerViewSet.as_view({'patch': 'partial_update'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 200)

    def test_edit_without_auth(self):
        request = self.factory.patch(f'/travelpartner/api/travelpartner/', {'name':'edited'})
        # force_authenticate(request, token=self.token.key)
        view = views.TravelPartnerViewSet.as_view({'patch': 'partial_update'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 204)


    def test_delete_without_auth(self):
        request = self.factory.delete(f'/travelpartner/api/travelpartner/')
        # force_authenticate(request, token=self.token.key)
        view = views.TravelPartnerViewSet.as_view({'delete': 'destroy'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 204)

    def test_delete(self):
        request = self.factory.delete(f'/travelpartner/api/travelpartner/', {'email':'edited@edited.com'})
        force_authenticate(request, token=self.token.key)
        view = views.TravelPartnerViewSet.as_view({'delete': 'destroy'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 203)



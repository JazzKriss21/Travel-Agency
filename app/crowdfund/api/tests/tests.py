from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from crowdfund.api.serializers import FundraiserSerializer
from crowdfund.models import Fundraiser
from crowdfund.api import views

from django.contrib.auth import get_user_model

from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

class CrowdfundTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create_user(
            email='user@foo.com', name='usertest', password='top_secret')
        self.id = self.user.id
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def test_get(self):
        request = self.factory.get('/crowdfund/api/fund/')
        force_authenticate(request, token=self.token.key)
        view = views.FundraiserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = {
        "user": '1',
        "title": "mock",
        "description": "mock",
        "date_goal": '2021-12-22',
        "amount_goal": "2000"
        }
        request = self.factory.post(f'/crowdfund/api/fund/', data)
        force_authenticate(request, token=self.token.key)
        view = views.FundraiserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_edit(self):
        request = self.factory.patch(f'/crowdfund/api/fund/', {'title':'edited'})
        force_authenticate(request, token=self.token.key)
        view = views.FundraiserViewSet.as_view({'patch': 'partial_update'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 200)

    def test_edit_without_auth(self):
        request = self.factory.patch(f'/crowdfund/api/fund/', {'title':'edited'})
        # force_authenticate(request, token=self.token.key)
        view = views.FundraiserViewSet.as_view({'patch': 'partial_update'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 204)


    def test_delete_without_auth(self):
        request = self.factory.delete(f'/crowdfund/api/fund/')
        # force_authenticate(request, token=self.token.key)
        view = views.FundraiserViewSet.as_view({'delete': 'destroy'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 204)

    def test_delete(self):
        request = self.factory.delete(f'/crowdfund/api/fund/')
        force_authenticate(request, token=self.token.key)
        view = views.FundraiserViewSet.as_view({'delete': 'destroy'})
        response = view(request,pk=self.user.id)
        self.assertEqual(response.status_code, 203)



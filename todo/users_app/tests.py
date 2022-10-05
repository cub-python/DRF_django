import math
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserViewSet
from .models import User, Biography


class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_12345'

        self.data = {'first_name': 'Gottleb', 'last_name': 'Daimler', 'email': 'gdimler@gmail.com'}
        self.data_put = {'first_name': 'Nikola', 'last_name': 'Daimler', 'email': 'nikola@gmail.com'}
        self.url = '/api/users/'
        self.admin = User.objects.create_superuser(self.name, self.password)

    # APIRequestFactory
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_quest(self):
        factory = APIRequestFactory()
        request = factory.post(self.url, {'name': 'Gottleb', 'email': 'gdimler@gmail.com'}, format='json')
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # APIClient
    def test_get_detail(self):
        user = User.objects.create(**self.data)
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


#
#
# #
# #     # APISimpleTestCase
class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        self.assertEqual(math.sqrt(4), 2)

#
#     # APItestCase
class TestBiography(APITestCase):

    def setUp(self) -> None:
        self.name = 'admin'
        self.password = 'admin_12345'

        self.data = {'first_name': 'Gottleb', 'last_name': 'Daimler', 'email': 'gdimler@gmail.com'}
        self.data_put = {'first_name': 'Nikola', 'last_name': 'Daimler', 'email': 'nikola@gmail.com'}
        self.url = '/api/biography/'
        self.admin = User.objects.create_superuser(self.name, self.password)

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_put_admin(self):
#         user = User.objects.create(**self.data)
#         bio = Biography.objects.create(text='test', user=user)
#         self.client.login(username=self.name, password=self.password)
#         response = self.client.put(f'{self.url}{bio.id}/', {'text': 'Biography', 'user': bio.user.id})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         bio_ = Biography.objects.get(id=bio.id)
#         self.assertEqual(bio_.text, 'Biography')
#         self.client.logout()
# #
        def test_put_mixer(self):
            bio = mixer.blend(Biography)
            self.client.login(username=self.name, password=self.password)
            response = self.client.put(f'{self.url}{bio.id}/', {'text': 'Biography', 'user': bio.author.id})
            self.assertEqual(response.status_code, status.HTTP_200_OK)

            bio_ = Biography.objects.get(id=bio.id)
            self.assertEqual(bio_.text, 'Biography')
            self.client.logout()

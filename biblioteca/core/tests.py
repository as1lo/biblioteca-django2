from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Colecao

class ColecaoTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_criar_colecao(self):
        data = {'nome': 'Minha Coleção', 'descricao': 'Descrição'}
        response = self.client.post('/colecoes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], 'Minha Coleção')

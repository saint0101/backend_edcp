# -*- encoding: utf-8 -*-

"""
Test pour les points de terminaison user
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from django.core.files.uploadedfile import SimpleUploadedFile


# URL pour créer un utilisateur (app_name='user)
CREATE_USER_URL = reverse('user:create')

# URL pour créer du token
TOKEN_URL = reverse('user:token')


# URL pour l'utilisateur
ME_URL = reverse('user:me')

def create_user(**params):
    """
        Création de nouvel utilisateur de test
    """

    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """ Tests publics de l'API utilisateur. """


    def setUp(self):
        """ Configuration initiale des tests """
        self.client = APIClient()  # Crée un client API pour effectuer les requêtes HTTP


    def test_create_user_success(self):
        """ Création d'un utilisateur avec succès """

        # Crée un fichier avatar non vide
        avatar_content = b'Ceci est un contenu d\'avatar de test'
        payload = {
            'email': 'user1@example.com',
            'login': 'sample1230',
            # 'role': 1,
            'avatar': SimpleUploadedFile(name='test_avatar.jpg', content=avatar_content, content_type='image/jpeg'),
            'nom': 'Doe',
            'prenoms': 'John',
            'organisation': 'XYZ Corp',
            'telephone': '+1234567890',
            'fonction': 'Manager',
            'consentement': 'Yes',
            'is_active': True,
            'is_staff': False,
            'password': 'mptestuser123'
        }
        res = self.client.post(CREATE_USER_URL, payload, format='multipart')  # Envoie une requête POST pour créer un utilisateur

        # Ajoutez cette ligne pour voir le message d'erreur
        # print('Erreur :', res.data)

        # Vérifie si la création de l'utilisateur a renvoyé le statut HTTP 201 (Créé)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # Récupère l'utilisateur nouvellement créé de la base de données
        user = get_user_model().objects.get(email=payload['email'])

        # Vérifie si le mot de passe de l'utilisateur correspond au mot de passe fourni
        self.assertTrue(user.check_password(payload['password']))

        # Vérifie que le mot de passe n'est pas retourné dans les données de la réponse
        self.assertNotIn('password', res.data)


    def test_user_with_email_exists_error(self):
        """Test si l'email de l'utilisateur existe, cela doit renvoyer une erreur"""

        payload = {
            'login': 'saint_doe',
            # 'role': 1,
            'avatar': SimpleUploadedFile(name='avatar.jpg', content=b'Test avatar content', content_type='image/jpeg'),
            'nom': 'Doe',
            'prenoms': 'John',
            'organisation': 'XYZ Corp',
            'telephone': '+1234567890',
            'fonction': 'Manager',
            'consentement': 'Yes',
            'email': 'test@example.com',
            'password': 'mptestuser123'
        }

        create_user(**payload)  # Crée un utilisateur avec l'email de test
        res = self.client.post(CREATE_USER_URL, payload, format='multipart')  # Envoie une requête POST pour créer un utilisateur
        # print('ERROR: ', res.data, res.status_code)
        # Vérifie si la création de l'utilisateur a renvoyé le statut HTTP 400 (Mauvaise requête)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_password_too_short_error(self):
        """Test la création d'un utilisateur avec un mot de passe trop court"""

        payload = {
            'email': 'user2@example.com',
            'login': 'sample1231',
            # 'role': 1,
            'avatar': SimpleUploadedFile(name='test_avatar.jpg', content=b'Test avatar content', content_type='image/jpeg'),
            'nom': 'Doe',
            'prenoms': 'John',
            'organisation': 'XYZ Corp',
            'telephone': '+1234567890',
            'fonction': 'Manager',
            'consentement': 'Yes',
            'is_active': True,
            'is_staff': False,
            'password': 'pwd'
        }

        res = self.client.post(CREATE_USER_URL, payload, format='multipart')  # Envoie une requête POST pour créer un utilisateur

        # Vérifie si la création de l'utilisateur a renvoyé le statut HTTP 400 (Mauvaise requête)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        # Vérifie que l'utilisateur n'existe pas
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)


    def test_create_token_for_user(self):
        """
            Test de creation d'un Token pour un user
        """
        user_details = {
            'email': 'user2@example.com',
            'login': 'sample1231',
            # 'role': 1,
            'avatar': SimpleUploadedFile(name='test_avatar.jpg', content=b'Test avatar content', content_type='image/jpeg'),
            'nom': 'Doe',
            'prenoms': 'John',
            'organisation': 'XYZ Corp',
            'telephone': '+1234567890',
            'fonction': 'Manager',
            'consentement': 'Yes',
            'is_active': True,
            'is_staff': False,
            'password': 'pwdrtqwerty54#$'
        }

        # creation d el'utilisateur
        create_user(**user_details)
        # information de geerer le token
        payload = {
            'email': user_details['email'],
            'password':user_details['password'],
        }

        # Envoie une requête POST pour créer le TOKEN
        res = self.client.post(TOKEN_URL, payload)
        # Vérifie la présence du token dans les données de réponse
        self.assertIn('token', res.data)
        # Vérifie le code de statut de la réponse
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_create_token_bad_credentials(self):
        """
            Test de creation du token avec de mauvaise informations
        """
        user_details = {
            'email': 'user2@example.com',
            'login': 'sample1231',
            # 'role': 1,
            'avatar': SimpleUploadedFile(name='test_avatar.jpg', content=b'Test avatar content', content_type='image/jpeg'),
            'nom': 'Doe',
            'prenoms': 'John',
            'organisation': 'XYZ Corp',
            'telephone': '+1234567890',
            'fonction': 'Manager',
            'consentement': 'Yes',
            'is_active': True,
            'is_staff': False,
            'password': 'pwdrtqwerty54@'
        }
          # creation d el'utilisateur
        create_user(**user_details)
        payload = {
            'email': user_details['email'],
            'password':'badpassword',
        }
        res = self.client.post(TOKEN_URL, payload)
        # Vérifie la présence du token dans les données de réponse
        self.assertNotIn('token', res.data)
        # Vérifie le code de statut de la réponse
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_token_blank_password(self):
        """Teste le retour d'erreur si un mot de passe vide est fourni."""

        # Prépare les données avec un mot de passe vide
        user_details = {
            'email': 'user2@example.com',
            'login': 'sample1231',
            # 'role': 1,
            'avatar': SimpleUploadedFile(name='test_avatar.jpg', content=b'Test avatar content', content_type='image/jpeg'),
            'nom': 'Doe',
            'prenoms': 'John',
            'organisation': 'XYZ Corp',
            'telephone': '+1234567890',
            'fonction': 'Manager',
            'consentement': 'Yes',
            'is_active': True,
            'is_staff': False,
            'password': 'pwd'
        }
          # creation d el'utilisateur
        create_user(**user_details)

        payload = {'email': 'test@example.com', 'password': ''}
        res = self.client.post(TOKEN_URL, payload)

        # Vérifie que le token n'est pas dans la réponse et que le statut de la requête est HTTP 400 (Bad Request)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_retrieve_user_unauthorized(self):
        """ Tester l'authorisatio require pour les utiisateurs """

        # Envoie une requête HTTP GET à l'URL spécifiée par ME_URL en utilisant le client de test intégré de Django.
        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    """ Tester les requêtes des utilisateurs qui nécessitent une authentification """

    def setUp(self):
        """ Configurer les paramètres de test """
        # Création d'un utilisateur de test
        self.user = create_user(
            login='saint_doe',
            # role=1,
            avatar=SimpleUploadedFile(name='avatar.jpg', content=b'Test avatar content', content_type='image/jpeg'),
            nom='Doe',
            prenoms='John',
            organisation='XYZ Corp',
            telephone='+1234567890',
            fonction='Manager',
            consentement='Yes',
            email='test@example.com',
            password='mptestuser123'

        )

        # Initialisation du client API pour effectuer des requêtes
        self.client = APIClient()
        # Authentification forcée avec l'utilisateur de test
        self.client.force_authenticate(user=self.user)






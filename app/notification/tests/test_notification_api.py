"""
Test pour la gestion des notifications
"""
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse # Importation de reverse pour gérer les URLs dynamiquement
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User

# Importation du modèle Token pour l'authentification par jeton
from rest_framework.authtoken.models import Token

from edcp_apirest.models import Notification
from django.core.files.uploadedfile import SimpleUploadedFile



# Utilisation de reverse pour générer l'URL
URL_CREATE_NOTIF = reverse('notification:notification-create')

# Utilisation de reverse pour générer l'URL pour la liste
URL_LIST_NOTIF = reverse('notification:notification-list')

# Récupère le modèle utilisateur personnalisé
User = get_user_model()


class NotificationTests(TestCase):
    """ Test des actons de la notification """

    def setUp(self):
        """Configuration initiale pour les tests"""

       # Crée un fichier avatar non vide
        avatar_content = b'Ceci est un contenu d\'avatar de test'
        avatar_file = SimpleUploadedFile(name='test_avatar.jpg', content=avatar_content,
        content_type='image/jpeg')

        # Création d'un utilisateur de test avec les champs requis
        self.user = User.objects.create_user(
            email='fouriersaint@gmail.com',
            login='Saint225',
            role_id=1,
            avatar=avatar_file,
            nom='Fourier',
            prenoms='onesyme',
            organisation='ARTCI',
            telephone='0708406361',
            fonction='informaticien',
            consentement='Yes',
            is_active=True,
            is_staff=False,
            password='mptestuser123'
        )
        # Génération d'un jeton d'authentification pour l'utilisateur de test
        self.token = Token.objects.create(user=self.user)
         # Initialisation du client API pour simuler des requêtes
        self.client = APIClient()
        # Configuration des en-têtes de requête pour inclure le jeton d'authentification
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_notification(self):
        # Test pour créer une nouvelle notification
        response = self.client.post(URL_CREATE_NOTIF, {'message': 'New test message'})
        # Vérifie que le statut de la réponse est 201 (Created)
        self.assertEqual(response.status_code, 201)
        # Vérifie que trois notifications ont été créées (ajustez ce nombre en fonction de votre contexte)
        self.assertEqual(Notification.objects.count(), 1)
        # Vérifie que le message de la dernière notification créée correspond au message envoyé
        self.assertEqual(Notification.objects.latest('created_at').message, 'New test message')


    def test_list_notifications(self):
        """ Lister les notifications """
        response = self.client.get(URL_LIST_NOTIF)
        # Vérifie le status de la requette pour lister les notifications
        self.assertEqual(response.status_code, 200)
        # Verifie le nombre de notifications est 0
        self.assertEqual(len(response.data), 0)


    def test_update_notification(self):
        """ Test pour mettre à jour une notification (la marquer comme lue) """

        # Assurez-vous qu'il y a au moins une notification dans la base de données
        if Notification.objects.count() == 0:
            Notification.objects.create(user=self.user, message='Test notification', is_reade=False)
        # Récupère la première notification
        notification = Notification.objects.first()
        # Utilisation de reverse pour générer l'URL pour les details
        URL_DETAIL_NOTIF = reverse('notification:notification-update', args=[notification.id])
        # Envoie une requête PATCH à l'URL générée avec {'is_read': True} pour mettre à jour
        # le champ is_read  de la notification
        response = self.client.patch(URL_DETAIL_NOTIF, {'is_reade': True})
        self.assertEqual(response.status_code, 200)
        notification.refresh_from_db()
        # Vérifie que le champ is_read est maintenant True
        self.assertTrue(notification.is_reade)





# -*- encoding: utf-8 -*-

"""
    Ecriture de la vue de l'utilisateur
"""

from rest_framework import generics, authentication, permissions

from rest_framework.authtoken.views import ObtainAuthToken

from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    """
        Creation d'un nouvelle utilisateur
    """
    serializer_class = UserSerializer


# Vue pour créer un jeton d'authentification
class CreateTokenView(ObtainAuthToken):
    """ serialiser les champs pour la creation du token """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# Vue pour gérer l'utilisateur authentifié
class ManageUserView(generics.RetrieveUpdateAPIView):
    """ Gestion de l'authentification de l'utilisateur."""

    serializer_class = UserSerializer  # Définit le sérialiseur pour la vue
    authentication_classes = [authentication.TokenAuthentication]  # Définit les classes d'authentification utilisées
    permission_classes = [permissions.IsAuthenticated]  # Définit les permissions requises pour accéder à la vue

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user

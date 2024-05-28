# -*- encoding: utf-8 -*-

"""
    Ecriture de la vue de l'utilisateur
"""

from rest_framework import generics
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

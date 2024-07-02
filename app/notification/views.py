# -*- encoding: utf-8 -*-

"""
    Ecriture de la vue des notifications
"""

from rest_framework import generics, permissions, authentication

from notification.serializers import NotificationSerializer
from edcp_apirest.models import Notification


class NotificationCreateView(generics.CreateAPIView):
    """ Vue pour créer une notification """

    serializer_class = NotificationSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Associe la notification à l'utilisateur authentifié
        serializer.save(user=self.request.user)


class NotificationListView(generics.ListAPIView):
    """ Vue pour lister les notifications """

    serializer_class = NotificationSerializer
    authentication_classes = [authentication.TokenAuthentication]  # Définit les classes d'authentification utilisées
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """ Récupère les notifications de l'utilisateur authentifié """
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')


class NotificationUpdateView(generics.UpdateAPIView):
    """ Vue pour mettre à jour une notification (par exemple, la marquer comme lue) """
    serializer_class = NotificationSerializer
    authentication_classes = [authentication.TokenAuthentication]  # Définit les classes d'authentification utilisées
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()

    def get_queryset(self):
        """ Récupère les notifications de l'utilisateur authentifié """
        return Notification.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        """ Marque la notification comme lue """
        serializer.instance.is_read = True
        serializer.save()
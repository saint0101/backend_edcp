# -*- encoding: utf-8 -*-

""" convertir les donnees en JSON """

from rest_framework import serializers

from edcp_apirest.models import Notification


# Sérialiseur pour le modèle de notification
class NotificationSerializer(serializers.ModelSerializer):
    """ serialiser les donnees de la table notification """

    class Meta:

        model = Notification
        # Champs à inclure dans le sérialiseur
        fields = ['id', 'user', 'message', 'created_at', 'is_reade']
        # user est en lecture seule car il sera ajouté automatiquement lors de la création
        read_only_fields = ['user']


    def create(self, validated_data):
        """
        Surcharger la méthode create pour ajouter automatiquement l'utilisateur
        à partir du contexte de la requête.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

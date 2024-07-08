# -*- encoding: utf-8 -*-

"""
    convertir les donnees en JSON
"""
from rest_framework import serializers

from user.serializers import UserSerializer
from edcp_apirest.models import (
    TypeClient,
    Secteur,
    Pays,
    Registration,
    Autorisation,
    )

# fields : Définir les champs à inclure dans la représentation JSON

# Serialiser les donnees de la table typec client
class TypeClientSerializer(serializers.ModelSerializer):
    """
        convertir en JSON les donnees de la table Typeclient
    """
    class Meta:
        model = TypeClient
        fields = '__all__'
        read_only_fields = ['id']


# Serialiser les donnees de la table Secteur
class SecteurSerializer(serializers.ModelSerializer):
    """
        convertir en JSON les donnees de la table Secteur
    """
    class Meta:
        model = Secteur
        fields = '__all__'
        read_only_fields = ['id']


# Serialiser les donnees de la table autorisation
class AutorisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autorisation
        fields = ['numero_autorisation',]


# Serialiser les donnees de la table Pays
class PaysSerializer(serializers.ModelSerializer):
    """
        convertir en JSON les donnees de la table Pays
    """
    class Meta:
        model = Pays
        fields = '__all__'
        read_only_fields = ['id']


# Serialiser les données de la table Registration
class RegistrationSerializer(serializers.ModelSerializer):
    """
        convertir en JSON les donnees de la table Registretion
    """
    typeClient = TypeClientSerializer(source='typeclient')  # Sérialiseur pour le type de client
    secteur = SecteurSerializer()  # Sérialiseur pour le secteur
    pays = PaysSerializer()  # Sérialiseur pour le pays
    autorisations = AutorisationSerializer(many=True, read_only=True)


    class Meta:
        model = Registration
        # Définition des champs à inclure dans la sérialisation
        fields = [
            'typeClient', 'raisonsociale', 'rccm', 'representant', 'telephone', 'email_contact', 'site_web',
            'secteur', 'effectif', 'presentation', 'pays', 'ville', 'adresse_geo', 'adresse_bp', 'gmaps_link', 'autorisations',
        ]
        # Définition des champs en lecture seule
        read_only_fields = ['id']  # Assurez-vous que 'user', 'typeclient', 'secteur' et 'pays' sont non modifiables

    def to_representation(self, instance):
        # Appel de la méthode parent pour obtenir la représentation de base
        representation = super().to_representation(instance)
        # Construction du dictionnaire de représentation personnalisée
        data = {
            "typeClient": {
                "id": representation['typeClient']['id'],
                "label": representation['typeClient']['label']
            },
            "nomRaisonSociale": representation['raisonsociale'],
            "numRccm": representation['rccm'],
            "representantLegal": representation['representant'],
            "telephone": representation['telephone'],
            "contactEmail": representation['email_contact'],
            "siteWeb": representation['site_web'],
            "secteur": {
                "id": representation['secteur']['id'],
                "label": representation['secteur']['label']
            },
            "effectif": str(representation['effectif']),  # Convertir en chaîne si nécessaire
            "presentation": representation['presentation'],
            "pays": {
                "id": representation['pays']['id'],
                "label": representation['pays']['label']
            },
            "ville": representation['ville'],
            "localisation": representation['adresse_geo'],
            "adresseBP": representation['adresse_bp'],
            "gmapsLink": representation['gmaps_link'],
            "autorisations": representation['autorisations']  # Inclure les autorisations
        }
        return data  # Retourner la représentation JSON personnalisée


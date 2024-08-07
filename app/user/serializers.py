# -*- encoding: utf-8 -*-

"""
Serialiser pou les utiisateurs
"""
from django.contrib.auth import (
    get_user_model, authenticate,
)

from django.utils.translation import gettext as _

from  rest_framework import serializers


# Définition du sérialiseur pour l'utilisateur
class UserSerializer(serializers.ModelSerializer):
    """Sérialiseur pour l'utilisateur."""

    class Meta:
        # Spécification du modèle et des champs à sérialiser
        model = get_user_model()
        fields = ('email', 'login', 'avatar', 'nom', 'prenoms', 'organisation', 'telephone', 'fonction', 'consentement', 'is_active', 'is_staff', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 10}}


    def create(self, validated_data):
        """Créer et retourner un utilisateur avec un mot de passe chiffré."""
        # Création d'un nouvel utilisateur avec les données validées
        return get_user_model().objects.create_user(**validated_data)


    def update(self, instance, validated_data):
        """ mettre ajour le mot de passe et retourener l'utiliateur"""
        # extraire le mot de passe et l'image  des données s'il est present
        password = validated_data.pop('password', None)

        # Appeler la méthode update de la classe parente pour mettre à jour les autres champs de l'instance
        user = super().update(instance, validated_data)
        # si le mode de passe de l'utilisateur a ete fournir
        if password:
            # mettre a jour le mot de passe de l'utilisateur avec le MP fournir
            user.set_password(password)
            # Sauvegarder l'instance de l'utilisateur pour appliquer le changement de mot de passe
            user.save()

        # Retourner l'instance de l'utilisateur mise à jour
        return user


# Définition du sérialiseur pour le jeton d'authentification de l'utilisateur
class AuthTokenSerializer(serializers.Serializer):
    """Sérialiseur pour le jeton d'authentification de l'utilisateur."""
    # Définition des champs 'email' et 'password'

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},  # Spécification du style du champ password
        trim_whitespace=False,  # Désactivation de la suppression des espaces blancs
    )

    def validate(self, attrs):
        """Valider et authentifier l'utilisateur."""

        # Récupération de l'e-mail et du mot de passe
        email = attrs.get('email')
        password = attrs.get('password')
        # Authentification de l'utilisateur
        user = authenticate(
            request=self.context.get('request'),  # Récupération de la requête
            email=email,
            password=password,
        )
        # Vérification de l'authentification
        if not user:
            # Si l'authentification échoue, une exception est levée
            msg = _("Impossible de s'authentifier avec les identifiants fournis.")
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs  # Retourne les attributs validés
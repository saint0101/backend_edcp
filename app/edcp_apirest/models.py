# -*- encoding: utf-8 -*-

"""
    Creation du model de la base de donnees
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Gestionnaire pour les utilisateurs"""


    def create_user(self, email, login, password=None, **extra_fields):
        """Crée, enregistre et retourne un nouvel utilisateur."""
        if not email:
            raise ValueError("L'utilisateur doit avoire une adresse email.")
        user = self.model(email=self.normalize_email(email), login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


        # Méthode pour créer un superutilisateur
    def create_superuser(self, email, login, password=None, **extra_fields):
        """Crée et enregistre un superutilisateur avec les informations fournies."""
        # Assurer que l'utilisateur est un membre du personnel et un superutilisateur
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Vérification des droits de superutilisateur
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Les superutilisateurs doivent avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Les superutilisateurs doivent avoir is_superuser=True.')

        # Création de l'utilisateur avec les droits de superutilisateur
        return self.create_user(email, login, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Utilisateur de la BD """

    login = models.CharField(max_length=100, unique=True)
    role_id = models.IntegerField(default=1)
    avatar = models.FileField(upload_to='avatars/', max_length=255, null=True, blank=True)
    nom = models.CharField(max_length=225)
    prenoms = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255, null=True, blank=True)
    telephone = models.CharField(max_length=100, null=True, blank=True)
    fonction = models.CharField(max_length=255, null=True, blank=True)
    consentement = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # extenssier la gestionnaire d'utilisateur
    objects = UserManager()

    # USERNAME_FIELD est défini sur 'email' pour l'authentification par e-mail.
    # REQUIRED_FIELDS spécifie les champs supplémentaires requis
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
            'login',
            'role_id',
            'nom',
            'prenoms',
            'organisation',
            'telephone',
            'fonction',
            'consentement',
        ]

    def __str__(self):
        """ les champs a retourner """
        # , self.nom, self.organisation, self.telephone, self.fonction
        return self.email
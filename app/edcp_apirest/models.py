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


class Role(models.Model):
    role = models.CharField(max_length=100)


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

    login = models.CharField(max_length=100, unique=True, verbose_name='Nom d\'Utilisateur')
    avatar = models.FileField(upload_to='avatars/', max_length=255, null=True, blank=True, verbose_name='Avatar')
    nom = models.CharField(max_length=225, verbose_name='Nom')
    prenoms = models.CharField(max_length=255, verbose_name='Prénoms')
    organisation = models.CharField(max_length=255, null=True, blank=True, verbose_name='Organisation')
    telephone = models.CharField(max_length=100, null=True, blank=True, verbose_name='Téléphone')
    fonction = models.CharField(max_length=255, null=True, blank=True, verbose_name='Fonction')
    consentement = models.CharField(max_length=255, null=True, blank=True, verbose_name='Consentement')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    is_active = models.BooleanField(default=True, verbose_name='Est Actif')
    is_staff = models.BooleanField(default=False, verbose_name='Est Membre du Personnel')

    class Meta:
        """ définir le nom singulier et pluriel du modèle """
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    # extenssier la gestionnaire d'utilisateur
    objects = UserManager()

    # USERNAME_FIELD est défini sur 'email' pour l'authentification par e-mail.
    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS spécifie les champs supplémentaires requis
    REQUIRED_FIELDS = [
            'login',
            # 'role',
            'nom',
            'prenoms',
            'organisation',
            'telephone',
            'fonction',
            'consentement',
        ]

    def __str__(self):
        """ les champs a retourner """
        # self.nom, self.organisation, self.telephone, self.fonction
        return self.nom


class Notification(models.Model):
    """ Table notification """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', verbose_name='Utilisateur') # Référence à l'utilisateur recevant la notification
    message = models.TextField() # message de notification
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date et heure de création')  # Date et heure de création de la notification
    is_read = models.BooleanField(default=False, verbose_name='Est lu')    # Indique si la notification a été lue

    def __str__(self):
        """ les champs à retourner """
        return f'Notification for {self.user} - {self.message}'

class TypeClient(models.Model):
    """ Table du type des clients """
    label = models.CharField(max_length=100, verbose_name='Type de Client')
    description = models.CharField(max_length=100, null=True, verbose_name='Description du Type de Client')
    sensible = models.BooleanField(null=True, verbose_name='Est Sensible')
    ordre = models.IntegerField(null=True, verbose_name='Ordre d\'Affichage')

    class Meta:
        """ définir le nom singulier et pluriel du modèle """
        verbose_name = 'Type Client'
        verbose_name_plural = 'Type Clients'

    def __str__(self):
        """ les champs a retourner """
        return self.label


class Secteur(models.Model):
    """ Table secteur d'activité """
    label = models.CharField(max_length=100, verbose_name='Secteur d\'Activité')
    sensible = models.BooleanField(verbose_name='Est Sensible')
    ordre = models.IntegerField(verbose_name='Ordre d\'Affichage')

    class Meta:
        """ définir le nom singulier et pluriel du modèle """
        verbose_name = 'Secteur'
        verbose_name_plural = 'Secteurs'

    def __str__(self):
        """ les champs a retourner """
        return self.label


class Pays(models.Model):
    """ Table des pays """
    label = models.CharField(max_length=100, verbose_name='Nom du Pays')

    class Meta:
        """ définir le nom singulier et pluriel du modèle """
        verbose_name = 'Pays'
        verbose_name_plural = 'Pays'

    def __str__(self):
        """ les champs a retourner """
        return self.label


class Registration(models.Model):
    """ Table enregistrement """
    # Lien vers l'utilisateur
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Utilisateur')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date de Création')
    # Lien vers le type de client
    typeclient = models.ForeignKey('TypeClient', on_delete=models.CASCADE, null=True, verbose_name='Type de Client')
    raisonsociale = models.CharField(max_length=100, verbose_name='Raison Sociale')
    representant = models.CharField(max_length=100, verbose_name='Représentant')
    rccm = models.CharField(max_length=100, null=True, verbose_name='RCCM')
    # Lien vers le secteur d'activité
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE, null=True, verbose_name='Secteur d\'Activité')
    secteur_description = models.CharField(max_length=100, null=True, verbose_name='Description du Secteur')
    presentation = models.CharField(max_length=255, null=True, verbose_name='Présentation')
    telephone = models.CharField(max_length=20, null=True, verbose_name='Téléphone')
    email_contact = models.CharField(max_length=100, null=True, verbose_name='Email de Contact')
    site_web = models.CharField(max_length=100, null=True, verbose_name='Site Web')
    # Lien vers le pays
    pays = models.ForeignKey('Pays', on_delete=models.CASCADE, null=True, verbose_name='Pays')
    ville = models.CharField(max_length=100, null=True, verbose_name='Ville')
    adresse_geo = models.CharField(max_length=100, null=True, verbose_name='Adresse Géographique')
    adresse_bp = models.CharField(max_length=100, null=True, verbose_name='Boîte Postale')
    gmaps_link = models.CharField(max_length=255, null=True, verbose_name='Lien Google Maps')
    effectif = models.IntegerField(null=True, verbose_name='Effectif')


    class Meta:
        """ définir le nom singulier et pluriel du modèle """
        verbose_name = 'Enregistrement'
        verbose_name_plural = 'Enregistrements'

    def __str__(self):
        """ les champs a retourner """
        return self.raisonsociale


class Autorisation(models.Model):
    registration = models.ForeignKey(Registration, related_name='autorisations', on_delete=models.CASCADE)
    numero_autorisation = models.CharField(max_length=20)  # Format : YYYY-NNNN
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Autorisation {self.numero_autorisation} pour {self.registration}"

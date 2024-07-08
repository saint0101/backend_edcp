# -*- encoding: utf-8 -*-

"""
Personnalisation de l'administration Django.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from django.conf import settings

# Importe les modèles ici
from edcp_apirest import models

# modeule enregistreprement d'un utilisateur
class UserAdmin(BaseUserAdmin):
    """
    Définit les pages d'administration pour les utilisateurs.
    """
    ordering = ['id']  # Ordonne les utilisateurs par ID
    list_display = ['email', 'login', 'organisation', 'consentement']  # Affiche les utilisateurs par e-mail et login

    # Éditer l'utilisateur
    fieldsets = (
        (None, {'fields': ('email', "password")}),  # Informations de connexion
        (
            _('Personal Info'),  # Titre pour les champs d'informations personnelles
            {
                'fields': (
                    'nom',
                    'prenoms',
                    'organisation',
                    'telephone',
                    'fonction',
                    'consentement',
                    'login',
                    # 'role',
                    'avatar',
                )
            }
        ),
        (
            _('Permissions'),  # Titre pour les champs de permission
            {
                'fields': (
                    'is_active',    # Active ou désactive le compte
                    'is_staff',     # Accorde l'accès au site d'administration
                    'is_superuser', # Accorde tous les accès
                )
            }
        ),
        (_('Dates importantes'), {'fields': ('last_login',)}),  # Date de dernière connexion
    )
    readonly_fields = ['last_login']  # Affiche la dernière connexion en lecture seule

    # Ajout d'un utilisateur
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'nom',
                'prenoms',
                'organisation',
                'telephone',
                'fonction',
                'consentement',
                'login',
                # 'role',
                'avatar',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

# module notificaton
class NotificationAdmin(admin.ModelAdmin):
    """ definir la page de l'administrateur """

    ordering = ['id']  # Ordonne les notifications par ID
    list_display = ['user', 'message', 'created_at', 'is_read']  # Affiche les utilisateurs par user et message

    # Éditer l'utilisateur
    fieldsets = (
        (None, {
            'fields': ('user', 'message', 'is_read')
        }),
    )


# module TypeClient
class TypeClientAdmin(admin.ModelAdmin):
    """ definir la page de l'administrateur """

    ordering = ['id']  # Ordonne les notifications par ID
    list_display = ['label', 'description', 'sensible', 'ordre']  # Affiche informatons de la table

    # Éditer le type du client
    fieldsets = (
        (None, {
            'fields': ('label', 'description', 'sensible', 'ordre')
        }),
    )


# module Secteur
class SecteurAdmin(admin.ModelAdmin):
    """ definir la page de l'administrateur """

    ordering = ['id']  # Ordonne les notifications par ID
    list_display = ['label', 'sensible', 'ordre']  # Affiche informatons de la table

    # Éditer le type du client
    fieldsets = (
        (None, {
            'fields': ('label', 'sensible', 'ordre')
        }),
    )


# module Autorisation
class AutorisationAdmin(admin.ModelAdmin):
    """ definir la page de l'administrateur """

    ordering = ['id']  # Ordonne les notifications par ID
    list_display = ['registration', 'numero_autorisation', 'created_at']  # Affiche informatons de la table

    # Éditer le type du client
    fieldsets = (
        (None, {
            'fields': ('registration', 'numero_autorisation', )
        }),
    )



# module Pays
class PaysAdmin(admin.ModelAdmin):
    """ definir la page de l'administrateur """

    ordering = ['id']  # Ordonne les notifications par ID
    list_display = ['label']  # Affiche informatons de la table

    # Éditer le type du client
    fieldsets = (
        (None, {
            'fields': ('label', )
        }),
    )


# module Registration
class RegistrationAdmin(admin.ModelAdmin):
    """ Page d'administration pour Registration """

    ordering = ['id']  # Ordonne les enregistrements par ID
    list_display = ['user', 'created_at', 'typeclient', 'raisonsociale', 'representant', 'rccm', 'secteur',
                    'secteur_description', 'presentation', 'telephone', 'email_contact', 'site_web', 'pays',
                    'ville', 'adresse_geo', 'adresse_bp', 'gmaps_link', 'effectif', ]

    fieldsets = (
        (None, {
            'fields': ('user', 'typeclient', 'raisonsociale', 'representant', 'rccm', 'secteur',
                       'secteur_description', 'presentation', 'telephone', 'email_contact', 'site_web', 'pays',
                       'ville', 'adresse_geo', 'adresse_bp', 'gmaps_link', 'effectif',)
        }),
    )


# Enregistrer le modèle Autorisation avec l'interface d'administration
admin.site.register(models.Autorisation, AutorisationAdmin)

# Enregistrer le modèle RegistrationAdmin avec l'interface d'administration
admin.site.register(models.Registration, RegistrationAdmin)

# Enregistrer le modèle PaysAdmin avec l'interface d'administration
admin.site.register(models.Pays, PaysAdmin)

# Enregistrer le modèle SecteurAdmin avec l'interface d'administration
admin.site.register(models.Secteur, SecteurAdmin)

# Enregistrer le modèle TypeClientAdmin avec l'interface d'administration
admin.site.register(models.TypeClient, TypeClientAdmin)

# Enregistrer le modèle CustomUser avec l'interface d'administration
admin.site.register(models.User, UserAdmin)

# Enregistrer le modèle CustomUser avec l'interface d'administration
admin.site.register(models.Notification, NotificationAdmin)

# Modifiez le titre de la page d'administration
admin.site.site_title = getattr(settings, 'ADMIN_SITE_TITLE', 'Django administration')
# Modifiez le titre affiché en haut de chaque page d'administration
admin.site.site_header = getattr(settings, 'ADMIN_SITE_HEADER', 'Django administration')
# Modifiez le texte affiché en haut de l'index du site d'administration
admin.site.index_title = getattr(settings, 'ADMIN_INDEX_TITLE', 'Site administration')




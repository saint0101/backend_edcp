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
    list_display = ['user', 'message', 'created_at', 'is_reade']  # Affiche les utilisateurs par user et message

    # Éditer l'utilisateur
    fieldsets = (
        (None, {
            'fields': ('user', 'message', 'is_reade')
        }),
    )

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




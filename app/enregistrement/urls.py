from django.urls import path, include
from rest_framework.routers import DefaultRouter

from enregistrement.views import (
        TypeClientViewSet,
        SecteurViewSet,
        PaysViewSet,
        # RegistrationViewSet,
        RegistrationListViewSet,
        # RegistrationCreateViewSet,
        AutorisationViewSet
)


# le nom de mappage de l'url
app_name = 'enregistrement'

# Créer deux instances de DefaultRouter
router_typeclient = DefaultRouter()
router_secteur = DefaultRouter()
router_pays = DefaultRouter()
router_registration = DefaultRouter()
router_autorisation = DefaultRouter()


# Enregistrer les viewsets avec des préfixes distincts
router_typeclient.register(r'typeclient', TypeClientViewSet)
router_secteur.register(r'secteur', SecteurViewSet)
router_pays.register(r'pays', PaysViewSet)
router_autorisation.register(r'autorisation', AutorisationViewSet)

# router_registration.register(r'enrg', RegistrationViewSet)


urlpatterns = [
    # Inclure les routeurs avec leurs préfixes
    path('', include(router_typeclient.urls)),
    path('', include(router_secteur.urls)),
    path('', include(router_pays.urls)),
    path('', include(router_autorisation.urls)),


    path('list/', RegistrationListViewSet.as_view(), name='enregistrement-list'),

]
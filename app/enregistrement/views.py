from django.shortcuts import render

# Create your views here.

"""
    Ensembles de Vues (Viewsets)
"""
from rest_framework import permissions, authentication, viewsets, generics
from enregistrement.serializers import TypeClientSerializer, SecteurSerializer, PaysSerializer, RegistrationSerializer, AutorisationSerializer

from edcp_apirest.models import TypeClient, Secteur, Pays, Registration, Autorisation



class TypeClientViewSet(viewsets.ModelViewSet):
    """ affiche toute les type client """
    serializer_class = TypeClientSerializer
    queryset = TypeClient.objects.all()
    authentication_classes = [authentication.TokenAuthentication]  # Définit les classes d'authentification utilisées
    permission_classes = [permissions.IsAuthenticated]


class SecteurViewSet(viewsets.ModelViewSet):
    """ affiche toute les Secteur """
    serializer_class = SecteurSerializer
    queryset = Secteur.objects.all()
    authentication_classes = [authentication.TokenAuthentication]  # Définit les classes d'authentification utilisées
    permission_classes = [permissions.IsAuthenticated]


class AutorisationViewSet(viewsets.ModelViewSet):
    queryset = Autorisation.objects.all()
    serializer_class = AutorisationSerializer
    authentication_classes = [authentication.TokenAuthentication]  # Définit les classes d'authentification utilisées
    permission_classes = [permissions.IsAuthenticated]



class PaysViewSet(viewsets.ModelViewSet):
    """ affiche toute les Pays """
    serializer_class = PaysSerializer
    queryset = Pays.objects.all()
    authentication_classes = [authentication.TokenAuthentication]  # Définit les classes d'authentification utilisées
    permission_classes = [permissions.IsAuthenticated]


#class RegistrationViewSet(viewsets.ModelViewSet):
#    """ affiche toute les Registration """
#    serializer_class = RegistrationSerializer
#    queryset = Registration.objects.all()
#    authentication_classes = [authentication.TokenAuthentication]  # Définit les classes d'authentification utilisées
#    permission_classes = [permissions.IsAuthenticated]


class RegistrationListViewSet(generics.ListAPIView):
    """ affiche toute les Registration """
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all()
    authentication_classes = [authentication.TokenAuthentication]  # Définit les classes d'authentification utilisées
    permission_classes = [permissions.IsAuthenticated]
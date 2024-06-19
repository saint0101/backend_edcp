# -*- encoding: utf-8 -*-

"""
    Ecriture des url
"""

from django.urls import path

from user import views

# le nom de mappage de l'url
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]


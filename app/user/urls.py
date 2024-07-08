# -*- encoding: utf-8 -*-

"""
    Ecriture des url
"""

from django.urls import path

from user.views import CreateUserView, CreateUserView, ManageUserView

# le nom de mappage de l'url
app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateUserView.as_view(), name='token'),
    path('manage/', ManageUserView.as_view(), name='me'),
]

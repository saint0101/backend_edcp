# -*- encoding: utf-8 -*-

"""
    Ecriture des url
"""

from django.urls import path, include

from notification.views import (
    NotificationCreateView,
    NotificationListView,
    NotificationUpdateView,
    # NotificationallViewSet,
    NotificationDeleteView
)

## vue d'enssemble (ViewSet)
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('', NotificationallViewSet)

## vues génériques (generics)
# le nom de mappage de l'url
app_name = 'notification'

urlpatterns = [
    # vues génériques (generics)
    path('create/', NotificationCreateView.as_view(), name='notification-create'),
    path('list/', NotificationListView.as_view(), name='notification-list'),
    path('update/<int:pk>/', NotificationUpdateView.as_view(), name='notification-update'),
    path('delete/<int:pk>/', NotificationDeleteView.as_view(), name='notification-delete'),

    # vue d'enssemble (ViewSet)
    # path('', include(router.urls)),

]
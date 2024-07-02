# -*- encoding: utf-8 -*-

"""
    Ecriture des url
"""

from django.urls import path

from notification.views import (
    NotificationCreateView,
    NotificationListView,
    NotificationUpdateView,
)

# le nom de mappage de l'url
app_name = 'notification'

urlpatterns = [
    path('create/', NotificationCreateView.as_view(), name='notification-create'),
    path('list/', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/', NotificationUpdateView.as_view(), name='notification-update'),

]
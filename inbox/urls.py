from django.urls import path
from .views import UnreadMessagesView, UnreadNotificationsView

urlpatterns = [
    path('unread-messages/', UnreadMessagesView.as_view(), name='unread-messages'),
    path('unread-notifications/', UnreadNotificationsView.as_view(), name='unread-notifications'),
]

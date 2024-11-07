from django.urls import path
from .views import UnreadMessagesView, UnreadNotificationsView

urlpatterns = [
    path('unread-messages/<int:user_id>/', UnreadMessagesView.as_view(), name='unread-messages'),
    path('unread-notifications/<int:user_id>/', UnreadNotificationsView.as_view(), name='unread-notifications'),
]

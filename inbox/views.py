from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.models import Notification
from messaging.models import Message
from inbox.models import Inbox
from .serializers import MessageSerializer, NotificationSerializer


class UnreadMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        inbox = Inbox.objects.get(user=user)
        unread_messages = Message.objects.filter(recipient=inbox, is_read=False)
        serializer = MessageSerializer(unread_messages, many=True)
        return Response(serializer.data)

class UnreadNotificationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        inbox = Inbox.objects.get(user=user)
        unread_notifications = Notification.objects.filter(user=inbox, is_read=False)
        serializer = NotificationSerializer(unread_notifications, many=True)
        return Response(serializer.data)

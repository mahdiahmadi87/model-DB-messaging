from rest_framework.views import APIView
from rest_framework.response import Response
from messaging.models import Message
from .serializers import MessageSerializer
from user.models import User
from notifications.models import Notification
from .serializers import NotificationSerializer
from user.models import User


class UnreadMessagesView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        
        unread_messages = Message.objects.filter(recipient=user, is_read=False)
        serializer = MessageSerializer(unread_messages, many=True)
        return Response(serializer.data)


class UnreadNotificationsView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        
        unread_notifications = Notification.objects.filter(user=user, is_read=False)
        serializer = NotificationSerializer(unread_notifications, many=True)
        return Response(serializer.data)

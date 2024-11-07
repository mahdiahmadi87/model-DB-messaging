from pluginsApp.core import PluginBase
from rest_framework import serializers
from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'content', 'timestamp', 'is_read']

class ReadNotificationsPlugin(PluginBase):
    def get_notifications(self, user):
        unread_notifications = Notification.objects.filter(user=user, is_read=True)
        serializer = NotificationSerializer(unread_notifications, many=True)
        return serializer.data

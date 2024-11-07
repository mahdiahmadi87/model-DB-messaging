from rest_framework.views import APIView
from rest_framework.response import Response
from inbox.models import Inbox
from .loader import load_active_plugins

class NotificationsView(APIView):
    def get(self, request):
        plugins = load_active_plugins()
        notifications = []
        user = request.user
        inbox = Inbox.objects.get(user=user)
        for plugin in plugins:
            x = {str(plugin.name):[plugin.get_notifications(inbox)]}
            notifications.append(x)
        
        return Response(notifications)

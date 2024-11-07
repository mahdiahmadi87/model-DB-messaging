from django.urls import path
from .views import NotificationsView

urlpatterns = [
    path('notifications/', NotificationsView.as_view()),
]


from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.throttling import ScopedRateThrottle

from website.serializers import ApplicationSerializer
from website.services.telegram_service import send_application_notification


class ApplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "applications"

    def perform_create(self, serializer):
        application = serializer.save()
        send_application_notification(application)

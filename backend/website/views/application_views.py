from rest_framework import generics
from rest_framework.permissions import AllowAny

from website.serializers import ApplicationSerializer


class ApplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]


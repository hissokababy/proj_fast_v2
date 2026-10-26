from rest_framework import generics

from website.serializers import ApplicationSerializer
from website.services.application_service import get_all_applications


class ApplicationListAPIView(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return get_all_applications()


class ApplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer


class ApplicationDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return get_all_applications()


class ApplicationUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return get_all_applications()


class ApplicationDeleteAPIView(generics.DestroyAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return get_all_applications()
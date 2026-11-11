from django.shortcuts import get_object_or_404
from rest_framework import generics

from website.models import SEOSettings
from website.serializers import SEOSettingsSerializer


class SEOSettingsAPIView(generics.RetrieveAPIView):
    serializer_class = SEOSettingsSerializer

    def get_object(self):
        return get_object_or_404(
            SEOSettings.objects.order_by("pk")
        )
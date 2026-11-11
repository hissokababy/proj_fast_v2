from django.shortcuts import get_object_or_404
from rest_framework import generics

from website.models import SiteSettings
from website.serializers import SiteSettingsSerializer


class SiteSettingsAPIView(generics.RetrieveAPIView):
    serializer_class = SiteSettingsSerializer

    def get_object(self):
        return get_object_or_404(
            SiteSettings.objects.order_by("pk")
        )
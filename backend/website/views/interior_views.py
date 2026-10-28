from rest_framework import generics

from website.serializers import InteriorPhotoSerializer
from website.services.interior_service import get_all_interiors


class InteriorPhotoListAPIView(generics.ListAPIView):
    serializer_class = InteriorPhotoSerializer

    def get_queryset(self):
        return get_all_interiors()



from rest_framework import generics

from website.serializers import CertificateSerializer
from website.services.certificate_service import get_all_certificates


class CertificateListAPIView(generics.ListAPIView):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return get_all_certificates()
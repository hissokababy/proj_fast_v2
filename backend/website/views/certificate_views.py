from django.db.models import QuerySet
from rest_framework import generics

from website.models import Certificate
from website.serializers import CertificateSerializer
from website.services.certificate_service import get_all_certificates


class CertificateListAPIView(generics.ListAPIView):
    serializer_class = CertificateSerializer

    def get_queryset(self) -> QuerySet[Certificate]:
        return get_all_certificates()
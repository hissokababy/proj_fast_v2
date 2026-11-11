from django.db.models import QuerySet

from website.models import Certificate


def get_all_certificates() -> QuerySet[Certificate]:
    return Certificate.objects.filter(is_active=True)
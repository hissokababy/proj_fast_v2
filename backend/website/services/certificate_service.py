
from django.db.models import QuerySet

from website.models import Certificate, Teacher


def get_all_certificates() -> QuerySet[Teacher]:
    return Certificate.objects.all()

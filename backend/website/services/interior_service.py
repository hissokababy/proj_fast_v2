from django.db.models import QuerySet

from website.models import InteriorPhoto


def get_all_interiors() -> QuerySet[InteriorPhoto]:
    return InteriorPhoto.objects.all()
from django.db.models import QuerySet

from website.models import Event


def get_all_events() -> QuerySet[Event]:
    return Event.objects.filter(is_active=True)
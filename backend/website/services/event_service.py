from django.db.models import QuerySet

from website.models import Event, Teacher


def get_all_events() -> QuerySet[Teacher]:
    return Event.objects.all()
from django.db.models import QuerySet

from website.models import Teacher


def get_all_teachers() -> QuerySet[Teacher]:
    return Teacher.objects.all()


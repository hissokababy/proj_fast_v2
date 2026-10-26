from website.models import Teacher


def get_all_teachers():
    return Teacher.objects.all()

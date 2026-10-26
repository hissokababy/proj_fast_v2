from website.models import Application


def get_all_applications():
    return Application.objects.all()
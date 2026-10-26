
from website.models import Certificate


def get_all_certificates():
    return Certificate.objects.all()

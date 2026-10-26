from website.models import InteriorPhoto


def get_all_interiors():
    return InteriorPhoto.objects.all()
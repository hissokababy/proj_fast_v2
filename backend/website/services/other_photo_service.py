from website.models import OtherPhoto


def get_photo_by_key(key: str) -> OtherPhoto | None:
    return OtherPhoto.objects.filter(key=key).first()


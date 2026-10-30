from rest_framework import generics
from rest_framework.exceptions import NotFound

from website.serializers import OtherPhotoSerializer
from website.services.other_photo_service import get_photo_by_key


class OtherPhotoByKeyAPIView(generics.RetrieveAPIView):
    serializer_class = OtherPhotoSerializer
    lookup_field = "key"

    def get_object(self):
        key = self.kwargs["key"]
        photo = get_photo_by_key(key)

        if photo is None:
            raise NotFound("Изображение не найдено.")

        return photo



from rest_framework import generics

from website.serializers import TeacherSerializer
from website.services.teacher_service import get_all_teachers


class TeacherListAPIView(generics.ListAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        return get_all_teachers()

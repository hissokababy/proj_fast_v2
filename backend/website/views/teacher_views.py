from django.db.models import QuerySet
from rest_framework import generics

from website.models import Teacher
from website.serializers import TeacherSerializer
from website.services.teacher_service import get_all_teachers

class TeacherListAPIView(generics.ListAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self) -> QuerySet[Teacher]:
        return get_all_teachers()
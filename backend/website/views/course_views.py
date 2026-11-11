from django.db.models import QuerySet
from rest_framework import generics

from website.models import Course
from website.serializers import CourseSerializer


class CourseListAPIView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self) -> QuerySet[Course]:
        queryset = Course.objects.filter(is_active=True)

        if self.request.query_params.get("home") == "true":
            queryset = queryset.filter(show_on_home=True)

        return queryset
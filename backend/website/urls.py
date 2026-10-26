
from django.urls import path

from website.views.teacher_views import TeacherListAPIView

urlpatterns = [
    path("teachers/", TeacherListAPIView.as_view(), name="teacher-list"),
]

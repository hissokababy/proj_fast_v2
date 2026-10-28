
from django.urls import path

from website.views.certificate_views import CertificateListAPIView
from website.views.event_views import EventListAPIView
from website.views.teacher_views import TeacherListAPIView
from website.views.interior_views import InteriorPhotoListAPIView
from website.views.application_views import ApplicationCreateAPIView

urlpatterns = [
    path("teachers/", TeacherListAPIView.as_view(), name="teacher-list"),
    path("certificates/", CertificateListAPIView.as_view(), name="certificate-list"),
    path("events/", EventListAPIView.as_view(), name="event-list"),
    path("interiors/", InteriorPhotoListAPIView.as_view(), name="interior-list"),
    path("applications/create/", ApplicationCreateAPIView.as_view(), name="application-create"),
]

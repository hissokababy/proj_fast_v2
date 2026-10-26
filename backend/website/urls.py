
from django.urls import path

from website.views.certificate_views import CertificateListAPIView
from website.views.event_views import EventListAPIView
from website.views.teacher_views import TeacherListAPIView
from website.views.interior_views import (
    InteriorPhotoListAPIView,
    InteriorPhotoCreateAPIView,
    InteriorPhotoDetailAPIView,
    InteriorPhotoUpdateAPIView,
    InteriorPhotoDeleteAPIView,
)
from website.views.application_views import (
    ApplicationListAPIView,
    ApplicationCreateAPIView,
    ApplicationDetailAPIView,
    ApplicationUpdateAPIView,
    ApplicationDeleteAPIView,
)

urlpatterns = [
    path("teachers/", TeacherListAPIView.as_view(), name="teacher-list"),
    path("certificates/", CertificateListAPIView.as_view(), name="certificate-list"),
    path("events/", EventListAPIView.as_view(), name="event-list"),

    path("interiors/", InteriorPhotoListAPIView.as_view(), name="interior-list"),
    path("interiors/create/", InteriorPhotoCreateAPIView.as_view(), name="interior-create"),
    path("interiors/<int:pk>/", InteriorPhotoDetailAPIView.as_view(), name="interior-detail"),
    path("interiors/<int:pk>/update/", InteriorPhotoUpdateAPIView.as_view(), name="interior-update"),
    path("interiors/<int:pk>/delete/", InteriorPhotoDeleteAPIView.as_view(), name="interior-delete"),

    path("applications/", ApplicationListAPIView.as_view(), name="application-list"),
    path("applications/create/", ApplicationCreateAPIView.as_view(), name="application-create"),
    path("applications/<int:pk>/", ApplicationDetailAPIView.as_view(), name="application-detail"),
    path("applications/<int:pk>/update/", ApplicationUpdateAPIView.as_view(), name="application-update"),
    path("applications/<int:pk>/delete/", ApplicationDeleteAPIView.as_view(), name="application-delete"),
]

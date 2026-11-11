from django.urls import path

from website.views.teacher_views import TeacherListAPIView
from website.views.certificate_views import CertificateListAPIView
from website.views.event_views import EventListAPIView
from website.views.interior_views import InteriorPhotoListAPIView
from website.views.course_views import CourseListAPIView
from website.views.site_settings_views import SiteSettingsAPIView
from website.views.seo_views import SEOSettingsAPIView
from website.views.application_views import ApplicationCreateAPIView
from website.views.other_photo_views import OtherPhotoByKeyAPIView


urlpatterns = [
    path("teachers/", TeacherListAPIView.as_view(), name="teacher-list"),
    path("certificates/", CertificateListAPIView.as_view(), name="certificate-list"),
    path("events/", EventListAPIView.as_view(), name="event-list"),
    path("interiors/", InteriorPhotoListAPIView.as_view(), name="interior-list"),
    path("courses/", CourseListAPIView.as_view(), name="course-list"),
    path("site-settings/", SiteSettingsAPIView.as_view(), name="site-settings"),
    path("seo/", SEOSettingsAPIView.as_view(), name="seo-settings"),
    path("applications/create/", ApplicationCreateAPIView.as_view(), name="application-create"),
    path("other-photos/<slug:key>/", OtherPhotoByKeyAPIView.as_view(), name="other-photo-by-key"),
]
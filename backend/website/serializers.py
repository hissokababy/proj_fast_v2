
from rest_framework import serializers

from website.models import (
    Application,
    Certificate,
    Course,
    Event,
    InteriorPhoto,
    OtherPhoto,
    SEOSettings,
    SiteSettings,
    Teacher,
)


class LanguageSerializerMixin:
    def get_language(self):
        request = self.context.get("request")
        language = request.query_params.get("lang", "uz") if request else "uz"
        return language if language in ("uz", "ru") else "uz"

    def get_translated_value(self, obj, field):
        language = self.get_language()
        value = getattr(obj, f"{field}_{language}", "")
        return value or getattr(obj, f"{field}_ru", "")


class TeacherSerializer(LanguageSerializerMixin, serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ["id", "name", "photo", "description", "order"]

    def get_name(self, obj):
        return self.get_translated_value(obj, "name")

    def get_description(self, obj):
        return self.get_translated_value(obj, "description")


class CertificateSerializer(LanguageSerializerMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = ["id", "title", "description", "image", "order"]

    def get_title(self, obj):
        return self.get_translated_value(obj, "title")

    def get_description(self, obj):
        return self.get_translated_value(obj, "description")


class EventSerializer(LanguageSerializerMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["id", "title", "image", "description", "order"]

    def get_title(self, obj):
        return self.get_translated_value(obj, "title")

    def get_description(self, obj):
        return self.get_translated_value(obj, "description")


class InteriorPhotoSerializer(LanguageSerializerMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = InteriorPhoto
        fields = ["id", "title", "image", "order"]

    def get_title(self, obj):
        return self.get_translated_value(obj, "title")


class CourseSerializer(LanguageSerializerMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "image",
            "order",
            "show_on_home",
        ]

    def get_title(self, obj):
        return self.get_translated_value(obj, "title")

    def get_description(self, obj):
        return self.get_translated_value(obj, "description")


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            "id",
            "full_name",
            "phone",
            "utm_source",
            "utm_medium",
            "utm_campaign",
            "utm_term",
            "utm_content",
            "landing_page",
            "referrer",
            "language",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class OtherPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPhoto
        fields = ["title", "key", "image"]


class SiteSettingsSerializer(LanguageSerializerMixin, serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    working_hours = serializers.SerializerMethodField()

    class Meta:
        model = SiteSettings
        fields = [
            "site_name",
            "logo",
            "favicon",
            "phone",
            "email",
            "address",
            "latitude",
            "longitude",
            "working_hours",
            "instagram_url",
            "telegram_url",
            "facebook_url",
            "youtube_url",
            "yandex_maps_map_id",
        ]

    def get_address(self, obj):
        return self.get_translated_value(obj, "address")

    def get_working_hours(self, obj):
        return self.get_translated_value(obj, "working_hours")


class SEOSettingsSerializer(LanguageSerializerMixin, serializers.ModelSerializer):
    meta_title = serializers.SerializerMethodField()
    meta_description = serializers.SerializerMethodField()
    h1 = serializers.SerializerMethodField()

    class Meta:
        model = SEOSettings
        fields = ["meta_title", "meta_description", "h1"]

    def get_meta_title(self, obj):
        return self.get_translated_value(obj, "meta_title")

    def get_meta_description(self, obj):
        return self.get_translated_value(obj, "meta_description")

    def get_h1(self, obj):
        return self.get_translated_value(obj, "h1")

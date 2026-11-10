
from django.contrib import admin
from .models import (
    Teacher,
    Certificate,
    Event,
    InteriorPhoto,
    Course,
    Application,
    OtherPhoto,
    SiteSettings,
    SEOSettings,
)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name_ru", "name_uz", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name_ru", "name_uz")
    list_filter = ("is_active",)
    ordering = ("order",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "title_uz", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title_ru", "title_uz")
    list_filter = ("is_active",)
    ordering = ("order",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "title_uz", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title_ru", "title_uz")
    list_filter = ("is_active",)
    ordering = ("order",)


@admin.register(InteriorPhoto)
class InteriorPhotoAdmin(admin.ModelAdmin):
    list_display = ("title_ru", "title_uz", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("title_ru", "title_uz")
    list_filter = ("is_active",)
    ordering = ("order",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title_ru",
        "title_uz",
        "order",
        "is_active",
        "show_on_home",
    )
    list_editable = ("order", "is_active", "show_on_home")
    search_fields = ("title_ru", "title_uz")
    list_filter = ("is_active", "show_on_home")
    ordering = ("order",)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone",
        "status",
        "language",
        "created_at",
    )
    search_fields = ("full_name", "phone", "utm_source", "utm_campaign")
    list_filter = ("status", "language", "created_at")
    readonly_fields = (
        "created_at",
        "updated_at",
        "telegram_notified_at",
    )
    ordering = ("-created_at",)

    fieldsets = (
        ("Данные клиента", {
            "fields": ("full_name", "phone", "status", "language"),
        }),
        ("Рекламные данные", {
            "fields": (
                "utm_source",
                "utm_medium",
                "utm_campaign",
                "utm_term",
                "utm_content",
                "landing_page",
                "referrer",
            ),
        }),
        ("Уведомления и даты", {
            "fields": (
                "telegram_notified_at",
                "created_at",
                "updated_at",
            ),
        }),
    )


@admin.register(OtherPhoto)
class OtherPhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "key", "image")
    search_fields = ("title", "key")
    prepopulated_fields = {"key": ("title",)}


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "phone", "email")

    fieldsets = (
        ("Основное", {
            "fields": ("site_name", "logo", "favicon"),
        }),
        ("Контакты", {
            "fields": ("phone", "email"),
        }),
        ("Адрес", {
            "fields": (
                "address_uz",
                "address_ru",
                "latitude",
                "longitude",
            ),
        }),
        ("График работы", {
            "fields": ("working_hours_uz", "working_hours_ru"),
        }),
        ("Социальные сети", {
            "fields": (
                "instagram_url",
                "telegram_url",
                "facebook_url",
                "youtube_url",
            ),
        }),
        ("Яндекс Карты", {
            "fields": ("yandex_maps_api_key", "yandex_maps_map_id"),
        }),
    )


@admin.register(SEOSettings)
class SEOSettingsAdmin(admin.ModelAdmin):
    list_display = ("meta_title_ru", "meta_title_uz")

    fieldsets = (
        ("Русский язык", {
            "fields": (
                "meta_title_ru",
                "meta_description_ru",
                "h1_ru",
            ),
        }),
        ("Узбекский язык", {
            "fields": (
                "meta_title_uz",
                "meta_description_uz",
                "h1_uz",
            ),
        }),
    )

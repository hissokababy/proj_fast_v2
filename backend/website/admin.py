
from django.contrib import admin
from .models import Teacher, Certificate, Event, InteriorPhoto, Application


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)
    search_fields = ("name",)
    ordering = ("order",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
    search_fields = ("title",)
    ordering = ("order",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
    search_fields = ("title",)
    ordering = ("order",)


@admin.register(InteriorPhoto)
class InteriorPhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)
    search_fields = ("title",)
    ordering = ("order",)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "created_at")
    search_fields = ("full_name", "phone")
    readonly_fields = ("created_at",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)


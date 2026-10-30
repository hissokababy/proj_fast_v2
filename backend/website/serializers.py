
from rest_framework import serializers

from website.models import Application, Certificate, Event, InteriorPhoto, Teacher, OtherPhoto


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "id",
            "name",
            "photo",
            "description",
            "order",
        ]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id", "title", "image", "order"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "image", "description", "order"]


class InteriorPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteriorPhoto
        fields = ["id", "title", "image", "order"]


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "full_name", "phone", "created_at"]
        read_only_fields = ["id", "created_at"]


class OtherPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPhoto
        fields = ["title", "key", "image"]

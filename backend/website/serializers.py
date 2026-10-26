
from rest_framework import serializers

from website.models import Teacher


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

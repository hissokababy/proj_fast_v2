from rest_framework import generics

from website.serializers import EventSerializer
from website.services.event_service import get_all_events


class EventListAPIView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return get_all_events()
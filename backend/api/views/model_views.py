from rest_framework import generics
from django.contrib.auth.models import User

from ..models import Festival, Band, BandEntry
from ..serializers import (
    FestivalSerializer,
    BandSerializer,
    UserSerializer,
    BandEntrySerializer,
    BandListSerializer,
)


class FestivalList(generics.ListAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer


class BandList(generics.ListAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class FestivalDetails(generics.RetrieveAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    lookup_field = "id"


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"


class UserBandListView(generics.ListAPIView):
    serializer_class = BandListSerializer
    lookup_field = "user_id"

    def get_queryset(self):
        band_entries = BandEntry.objects.order_by("user", "band__festival").distinct(
            "user", "band__festival"
        )
        return [
            {"festival": entry.band.festival, "user": entry.user}
            for entry in band_entries
        ]


class FestivalBandListView(generics.ListAPIView):
    serializer_class = BandListSerializer
    lookup_field = "band__festival_id"

    def get_queryset(self):
        band_entries = BandEntry.objects.order_by("user", "band__festival").distinct(
            "user", "band__festival"
        )
        return [
            {"festival": entry.band.festival, "user": entry.user}
            for entry in band_entries
        ]


class BandListDetails(generics.ListAPIView):
    queryset = BandEntry.objects.all()
    serializer_class = BandEntrySerializer
    lookup_field = ["user_id", "band__festival_id"]

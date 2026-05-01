from rest_framework import generics

from ..models import Festival, Band
from ..serializers import FestivalSerializer, BandSerializer


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

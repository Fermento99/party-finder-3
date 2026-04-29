from rest_framework import generics
from .models import Festival, Band
from .serializers import FestivalSerializer, BandSerializer


class FestivalListCreate(generics.ListCreateAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer


class BandListCreate(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer


class FestivalDetails(generics.RetrieveAPIView):
    queryset = Festival.objects.all()
    serializer_class = FestivalSerializer
    lookup_field = "id"

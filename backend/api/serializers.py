from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Band, Festival, BandEntry


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = "__all__"


class FestivalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Festival
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "last_login", "date_joined", "is_active"]


class BandEntrySerializer(serializers.ModelSerializer):
    band = BandSerializer()
    user = UserSerializer()

    class Meta:
        model = BandEntry
        fields = ["band", "user", "grade"]


class BandListSerializer(serializers.Serializer):
    festival = FestivalSerializer()
    user = UserSerializer()

from rest_framework import serializers

from .models import Band, Festival


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = "__all__"


class FestivalSerializer(serializers.ModelSerializer):
    bands = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if type(self.context["view"]).__name__ != "FestivalDetails":
            self.fields.pop("bands")

    class Meta:
        model = Festival
        fields = "__all__"

    def get_bands(self, obj):
        bands = Band.objects.filter(festival_id=obj.id)
        return [BandSerializer(band).data for band in bands]

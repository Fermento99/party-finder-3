from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from .models import Band, Festival, BandEntry

admin.site.register(Festival)
admin.site.register(BandEntry)


class BandResource(resources.ModelResource):
    class Meta:
        model = Band
        widgets = {
            "day": {"format": "%d-%m-%Y"}
        }


@admin.register(Band)
class BandAdmin(ImportExportModelAdmin):
    resource_classes = [BandResource]

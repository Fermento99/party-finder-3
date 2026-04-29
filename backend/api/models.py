from django.db import models


class Festival(models.Model):
    name = models.CharField(max_length=35)
    year = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    lineup_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.year})"


class Band(models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    country_code = models.CharField(max_length=8, blank=True, null=True)
    stage = models.CharField(max_length=35, blank=True, null=True)
    day = models.DateField(blank=True, null=True)
    spotify_link = models.URLField(blank=True, null=True)
    lineup_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.festival.name})"

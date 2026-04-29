from django.urls import path

from .views import BandListCreate, FestivalListCreate, FestivalDetails

urlpatterns = [
    path("bands/", BandListCreate.as_view()),
    path("festivals/", FestivalListCreate.as_view()),
    path("festivals/<int:id>/", FestivalDetails.as_view()),
]

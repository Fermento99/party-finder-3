from django.urls import path

from .views.model_views import (
    BandList,
    FestivalList,
    FestivalDetails,
)
from .views.auth_views import (
    RegisterUser,
    LoginUser,
    logout_user,
)

urlpatterns = [
    # models
    path("bands/", BandList.as_view()),
    path("festivals/", FestivalList.as_view()),
    path("festivals/<int:id>/", FestivalDetails.as_view()),
    path("auth/register/", RegisterUser.as_view()),
    path("auth/login/", LoginUser.as_view()),
    path("auth/logout/", logout_user),
]

from django.urls import path

from .views.model_views import (
    BandListCreate,
    FestivalListCreate,
    FestivalDetails,
)
from .views.auth_views import (
    RegisterUser,
    LoginUser,
    logout_user,
)

urlpatterns = [
    path("bands/", BandListCreate.as_view()),
    path("festivals/", FestivalListCreate.as_view()),
    path("festivals/<int:id>/", FestivalDetails.as_view()),
    path("auth/register/", RegisterUser.as_view()),
    path("auth/login/", LoginUser.as_view()),
    path("auth/logout/", logout_user),
]

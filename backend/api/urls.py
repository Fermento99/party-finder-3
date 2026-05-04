from django.urls import path

from .views.model_views import (
    BandList,
    FestivalList,
    FestivalDetails,
    UsersList,
    UserDetails,
    UserBandListView,
    FestivalBandListView,
    FestivalBandsList,
    BandListDetails,
)
from .views.auth_views import (
    RegisterUser,
    LoginUser,
    logout_user,
)
from .views.action_views import (
    BandEntry,
)

urlpatterns = [
    # models
    path("bands/", BandList.as_view()),
    path("festivals/", FestivalList.as_view()),
    path("festivals/<int:id>/", FestivalDetails.as_view()),
    path("festivals/<int:band__festival_id>/lists", FestivalBandListView.as_view()),
    path("festivals/<int:festival_id>/bands", FestivalBandsList.as_view()),
    path("users/", UsersList.as_view()),
    path("users/<int:id>/", UserDetails.as_view()),
    path("users/<int:user_id>/lists/", UserBandListView.as_view()),
    path("lists/<int:user_id>/<int:band__festival_id>", BandListDetails.as_view()),
    # auth
    path("auth/register/", RegisterUser.as_view()),
    path("auth/login/", LoginUser.as_view()),
    path("auth/logout/", logout_user),
    # actions
    path("band-entry/", BandEntry.as_view()),
]

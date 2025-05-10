from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rewards.views import ProfileView

base_api = "api/"

urlpatterns = [
    path(
        f"{base_api}token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        f"{base_api}token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        f"{base_api}token/verify/",
        TokenVerifyView.as_view(),
        name="token_verify",
    ),
    path(
        f"{base_api}profile/",
        ProfileView.as_view(),
        name="profile",
    ),
]

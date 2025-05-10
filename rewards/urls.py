from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rewards.views import ProfileView, ScheduleRewardView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path(
        "rewards/request/", ScheduleRewardView.as_view(), name="reward_request"
    ),
]

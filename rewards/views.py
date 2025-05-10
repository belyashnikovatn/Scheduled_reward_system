from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rewards.serializers import ScheduleRewardSerializer
from rewards.models import ScheduleReward
from rest_framework.generics import CreateAPIView


class ProfileView(APIView):
    """
    View to get user profile information.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get user profile information.
        """
        user = request.user
        data = {
            "username": user.username,
            "email": user.email,
            "coins": user.coins,
        }
        return Response(data)


class ScheduleRewardView(CreateAPIView):
    """
    View to create a scheduled reward for a user.
    """

    queryset = ScheduleReward.objects.all()
    serializer_class = ScheduleRewardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the new scheduled reward instance.
        """
        serializer.save(user=self.request.user)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


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

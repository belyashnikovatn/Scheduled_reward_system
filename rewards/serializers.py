from django.utils import timezone
from rest_framework import serializers
from rewards.models import ScheduleReward


class ScheduleRewardSerializer(serializers.ModelSerializer):
    """
    Serializer for the ScheduleReward model.
    It validates the amount and execute_at fields.
    """

    class Meta:
        model = ScheduleReward
        fields = ["id", "user", "amount", "execute_at"]
        read_only_fields = ["user"]

    def validate_amount(self, value):
        """
        Validate that the amount is a positive integer.
        """
        if value <= 0:
            raise serializers.ValidationError(
                "Amount must be a positive integer."
            )
        return value

    def validate_execute_at(self, value):
        """
        Validate that the execute_at date is in the future.
        """
        if value <= timezone.now():
            raise serializers.ValidationError(
                "Executed at must be in the future."
            )
        return value

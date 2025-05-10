from datetime import timezone
from rest_framework import serializers
from rewards.models import ScheduleReward


class ScheduleRewardSerializer(serializers.ModelSerializer):
    """
    Serializer for the ScheduleReward model.
    It validates the amount and executed_at fields.
    """

    class Meta:
        model = ScheduleReward
        fields = ["id", "user", "amount", "executed_at"]

    def validate_amount(self, value):
        """
        Validate that the amount is a positive integer.
        """
        if value <= 0:
            raise serializers.ValidationError(
                "Amount must be a positive integer."
            )
        return value

    def validate_executed_at(self, value):
        """
        Validate that the executed_at date is in the future.
        """
        if value <= timezone.now():
            raise serializers.ValidationError(
                "Executed at must be in the future."
            )
        return value

    def create(self, validated_data):
        """
        Create a new ScheduleReward instance.
        """
        return ScheduleReward.objects.create(**validated_data)

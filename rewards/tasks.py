from celery import shared_task
from django.utils import timezone
from rewards.models import ScheduleReward, RewardLog


@shared_task
def execute_schedule_reward(reward_id):
    """
    Task to execute a scheduled reward for a user.
    """
    try:
        # Get the scheduled reward by ID
        reward = ScheduleReward.objects.get(id=reward_id)
    except ScheduleReward.DoesNotExist:
        return f"Reward with ID {reward_id} does not exist."

    if reward.executed_at > timezone.now():
        execute_schedule_reward.apply_async(
            (reward_id,), eta=reward.executed_at
        )
        return f"Reward with ID {reward_id} is rescheduled"

    user = reward.user
    user.coins += reward.amount
    user.save()

    RewardLog.objects.create(
        user=user,
        amount=reward.amount,
    )

    return f"Reward with ID {reward_id} executed successfully."

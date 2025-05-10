from rewards.models import ScheduleReward
from django.db.models.signals import post_save
from django.dispatch import receiver
from rewards.tasks import execute_schedule_reward


@receiver(post_save, sender=ScheduleReward)
def schedule_reward_created(sender, instance, created, **kwargs):
    """
    Signal receiver that triggers when a ScheduleReward is created.
    It schedules the task to execute the reward at the specified time.
    """
    if created:
        execute_schedule_reward.apply_async(
            (instance.id,), eta=instance.execute_at
        )

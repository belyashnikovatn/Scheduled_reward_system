from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """

    coins = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class ScheduleReward(models.Model):
    """
    Model representing a schedule for a user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    executed_at = models.DateTimeField()

    def __str__(self):
        return (
            f"{self.user.username} - {self.amount} coins on {self.executed_at}"
        )


class RewardLog(models.Model):
    """
    Model representing a log reward for a user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    given_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} coins on {self.given_at}"

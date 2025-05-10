from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    """

    coins = models.IntegerField(default=0)

    def __str__(self):
        return self.username

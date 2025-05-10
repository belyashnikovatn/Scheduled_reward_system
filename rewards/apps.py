from django.apps import AppConfig


class RewardsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "rewards"

    def ready(self):
        """
        This method is called when the app is ready.
        It imports the signals module to ensure that the signal handlers are registered.
        """
        import rewards.signals

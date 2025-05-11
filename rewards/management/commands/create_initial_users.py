from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "Creates initial admin and test users"

    def handle(self, *args, **options):
        # Создаем суперпользователя
        admin, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@example.com",
                "is_staff": True,
                "is_superuser": True,
                "coins": 1000,
            },
        )
        if created:
            admin.set_password("adminpass")
            admin.save()
            self.stdout.write(
                self.style.SUCCESS("Superuser created successfully")
            )
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists"))

        # Создаем тестовых пользователей
        users_data = [
            {
                "username": "Лея",
                "email": "leia@example.com",
                "password": "leiapass",
                "coins": 300,
            },
            {
                "username": "Хан Соло",
                "email": "hansolo@example.com",
                "password": "solopass",
                "coins": 200,
            },
            {
                "username": "Люк",
                "email": "luke@example.com",
                "password": "lukepass",
                "coins": 150,
            },
        ]

        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data["username"],
                defaults={
                    "email": user_data["email"],
                    "coins": user_data["coins"],
                },
            )
            if created:
                user.set_password(user_data["password"])
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f"User {user.username} created")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'User {user_data["username"]} already exists'
                    )
                )

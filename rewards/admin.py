from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ScheduleReward, RewardLog
from django.utils.html import format_html


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "coins", "is_staff", "date_joined")
    list_filter = ("is_staff", "is_superuser", "is_active", "date_joined")
    search_fields = ("username", "email")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {"fields": ("first_name", "last_name", "email", "coins")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "coins",
                ),
            },
        ),
    )


class ScheduleRewardAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "formatted_executed_at", "status")
    list_filter = ("executed_at",)
    search_fields = ("user__username", "user__email")
    date_hierarchy = "executed_at"
    readonly_fields = ("status",)

    def formatted_executed_at(self, obj):
        if obj.executed_at:
            return obj.executed_at.strftime("%Y-%m-%d %H:%M")
        return "Not scheduled"

    formatted_executed_at.short_description = "Executed At"

    def status(self, obj):
        from django.utils.timezone import now

        if obj.executed_at is None:
            return format_html(
                '<span style="color: gray;">Not scheduled</span>'
            )
        if obj.executed_at <= now():
            return format_html('<span style="color: green;">Completed</span>')
        return format_html('<span style="color: orange;">Pending</span>')

    status.short_description = "Status"

    def save_model(self, request, obj, form, change):
        if not obj.executed_at:
            obj.executed_at = None
        super().save_model(request, obj, form, change)


class RewardLogAdmin(admin.ModelAdmin):
    list_display = ("user", "amount", "formatted_given_at")
    list_filter = ("given_at",)
    search_fields = ("user__username", "user__email")
    date_hierarchy = "given_at"
    readonly_fields = ("given_at",)

    def formatted_given_at(self, obj):
        return obj.given_at.strftime("%Y-%m-%d %H:%M")

    formatted_given_at.short_description = "Given At"


admin.site.register(User, CustomUserAdmin)
admin.site.register(ScheduleReward, ScheduleRewardAdmin)
admin.site.register(RewardLog, RewardLogAdmin)
